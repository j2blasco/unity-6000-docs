import asyncio
import os
import re
import shutil
from crawl4ai import *

def safe_filename(url):
    return re.sub(r'[^a-zA-Z0-9]', '_', url)[:100] + ".md"

def cleanup_output_folder(output_dir):
    """Clean up the output folder before starting the crawl"""
    if os.path.exists(output_dir):
        print(f"Cleaning up existing content in {output_dir}...")
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output folder {output_dir} is ready.")

outputDirName = "docs"

async def main():
    # Clean up output folder first
    cleanup_output_folder(outputDirName)
    
    # CSS extraction strategy to target content-block div specifically
    
    filter_chain = FilterChain([
        URLPatternFilter(patterns=["*6000.0/Documentation*"]),
        ContentTypeFilter(allowed_types=["text/html"])
    ])


    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=5, 
            # max_pages=3,
            filter_chain=filter_chain
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        cache_mode=CacheMode.ENABLED,
        css_selector="div.content-block",
        excluded_selector="div.feedbackbox, div.footer-wrapper",
        markdown_generator=DefaultMarkdownGenerator(
            content_source="cleaned_html",
            content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed", min_word_threshold=0)
        ),
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(
            url="https://docs.unity3d.com/6000.0/Documentation/Manual/UnityManual.html",
            config=config
        )

        if not isinstance(results, list):
            return
        for i, result in enumerate(results):
            if not isinstance(result, CrawlResult):
                continue

            if result.success:
                filename = safe_filename(result.url)
                filepath = os.path.join(outputDirName, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"* Source: {result.url}\n\n")
                    f.write(str(result.markdown))
                
                print(f"Saved ({i+1}/{len(results)}): {filename}")
            else:
                print(f"Failed to process: {result.url if hasattr(result, 'url') else 'Unknown URL'}")

if __name__ == "__main__":
    asyncio.run(main())