---
title: "Migrating from WordPress to Hugo"
date: 2026-05-04
slug: wordpress-to-hugo-migration
description: "A deep dive into a 15-year-old WordPress blog migration to Hugo using the Blowfish theme and using Cloudflare Pages for hosting."
summary: "After 7 years of inactivity, I moved my legacy blog to a modern static stack. Here is how I handled 100+ posts, fixed SSG build crashes, and automated the cleanup."
categories:
- geek-on-web
showTableOfContents: true
draft: false
---

{{< lead >}}
After many years on WordPress, and almost 7 years of inactivity, I've finally moved my old blog to a modern, fast static site using Hugo and the Blowfish theme. This is the story of how I did it.
{{< /lead >}}

My ilantz.com domain was due for renewal, and I've been thinking for a while about taking the dust off my old blog and migrating it to a modern, faster, and ad-free platform. 

Overall, and with the help of AI, the initial research and migration was very fast, but the cleanup and the iterations to get to the final result took quite a few iterations. The initial migration itself (deciding on Hugo, converting WordPress content to Markdown, setting up a local development environment for Hugo, and finally deploying the new site on Cloudflare Pages) was very quick (just a few hours), but refining the output to what I was looking for took much longer.

Writing this blog post actually took longer than the migration itself :) I wanted to make sure I post it when I'm truly "done", making sure to document the challenges I encountered during the process, which I felt were worth sharing, including submitting PR's to fix them... 

It's been a while, and much has happened since my last post in 2019... But, I'm happy I finally got the drive to re-establish my blog and share some of my latest projects with you, starting with this one!

### **Getting out of WordPress**

I followed muffn_'s [How I Migrated From WordPress to Hugo](https://blog.muffn.io/posts/how-i-migrated-from-wordpress-to-hugo/) guide for the migration process. I recommend it if you're planning a similar move. This post aims to provide the additional details and learnings from my migration journey.

As noted in the guide, converting that to Markdown, as required by Hugo, can be a bit tricky. Luckily, we can use this great tool: {{< github repo="lonekorean/wordpress-export-to-markdown" showThumbnail=false >}}

Here's how I ran it against my WordPress xml export:

```bash
npx wordpress-export-to-markdown

```

These were the settings i ended up using to achieve the structure i wanted:

```bash
✓ Path to WordPress export file? ilantz-blog.xml
✓ Put each post into its own folder? Yes
✓ Add date prefix to posts? No
✓ Organize posts into date folders? Year and month folders
✓ Save images? All Images

```

And just like that, there's an `output` folder with all of my old WordPress posts converted to markdown files, along with all images organized in a folder structure based on the year and month they were published.

> [!NOTE]
> The wordpress-export-to-markdown tool pulls images from the source url's, so make sure your old WP site is up and running during the process.

### **Debugging the Hugo server crash**

Installing Hugo and Blowfish theme was straightforward, once my local development server was up, I just copied over all of the posts into the content directory.

But of course...it couldn't be that simple... as soon as I did that, the Hugo server started crashing with this error:

```bash
ERROR Failed to publish Resource: open /Users/username/ilantz-blog/public: is a directory
```

I realized its the migrated content, but figuring out which post caused the crash could have been a long process of trial and error... the error message didn't point to a specific post. Luckily, I could ask AI... :)

And so it turns out, the issue was pinned to a post from July 2010, which contained raw Windows registry keys that weren't formatted in code blocks, which the wordpress-export-to-markdown tool carried over. And apparently Hugo, as part of its "Page Bundle" processor, thought they were files it needed to publish... As mentioned above, I've submitted [PR #187](https://github.com/lonekorean/wordpress-export-to-markdown/pull/187) to the wordpress-export-to-markdown repo to help mitigate this for future users.

AI was a great help throughout this whole migration project. I explained the goal and details to the AI agent, "I'm migrating from WordPress to Hugo, using the Blowfish theme. I've used the wordpress-export-to-markdown tool to convert my WordPress posts to Markdown, and now the Hugo server is crashing with this error message (provided the error message). I moved a few of the posts and the server stopped crashing, so the issue is in one or more of the posts. Help me find it and solve the issue."

If you’re doing a similar migration, here are a few example prompts you can use; each one pretty much explains its purpose below.

---

#### Post wordpress-export-to-markdown fixes

If you’re doing a similar migration, using wordpress-export-to-markdown, consider these prompts to clean up the content, they were very helpful in my case.

> "Scan every `index.md` file in my `content/posts/` directory and perform the following updates to the content:
> 1. Identify any raw logs, registry keys, or file paths that aren't inside code blocks and wrap them in triple backticks (```).
> 2. Convert all WordPress `[caption]` shortcodes into Hugo `{{</* figure */>}}` shortcodes, ensuring the `src` and `caption` attributes are preserved.
> 3. Wrap the very first paragraph of every post in a `{{</* lead */>}}...{{</* /lead */>}}` shortcode to match the Blowfish theme style.
> 4. Normalize image URLs to ensure they point correctly to the local `images/` folder within each post bundle.
> 5. Compare all posts URLs against `ilantz-blog.xml`, the `<link>` tag lists the original post urls, fix any mismatching URL in the frontmatter."
> 

While these are great for one-off fixes, with so many posts, I had the agent consolidate them into one big script, which I placed in the scripts directory of the repo [sanitize_posts.py](https://github.com/ilantz/ilantz-blog/blob/main/scripts/sanitize_posts.py). It’s the result of several iterations with an AI agent to handle the various edge cases discovered during the migration process. Feel free to use it as-is, at your own risk :) , use it for context, or use it to create your own scripts.

While iterating over the posts, and since many of my technical posts contain long log files and registry paths, I've wanted to adjust the default, horizontal scrolling for code blocks, so I added a custom "line-wrap" toggle in the header, and turned it on by default for my blog. This allows you to toggle between the clean, standard horizontal scrolling and a wrapped view that makes long lines much easier to read in full.

Finally, as I added this control, I noticed that the dark/light mode control didn't had a tooltip like the search button did, so I asked AI and it helped fix that too, so I submitted [PR #2945](https://github.com/nunocoracao/blowfish/pull/2945) to the Blowfish theme repo.

---

### **Hosting on Cloudflare**

After all initial content was migrated successfully, and the crash fixed, I was ready to deploy. This blog now runs on **Cloudflare Pages**. It's super simple—every time I push a change to GitHub, the site builds and updates automatically. Whenever I'm done testing on my local machine, I just push to GitHub and it rebuilds and updates. Bye WordPress admin...

Cloudflare simplified their compute wizard, and finding the wizard to create a page is a bit hidden. Navigate to **Workers & Pages**, under Compute and click the "Create application" button. When the wizard opens, look for the "Looking to deploy Pages? Get started" at the very bottom of the screen. Click it, then choose to Import an existing Git repository and point to your GitHub repo.

There were also a few extra settings I had to tweak:

* **Pinning the Hugo Version**: Cloudflare defaults to an older version of Hugo that doesn't play nice with modern themes. I had to set the **`HUGO_VERSION`** environment variable to **`0.161.1`** in the Cloudflare dashboard.
* **BaseURL**: I made sure my `hugo.toml` had the `baseURL` set to `[https://ilantz.com/](https://ilantz.com/)` so all my links were generated correctly.
* **Build Command**: Updated the default hugo command to `hugo --gc --minify` to keep the site as fast and light as possible.

Feels good to finally have a modern, fast home for my "IT ramblings."

Thanks for visiting! :)

ilantz
