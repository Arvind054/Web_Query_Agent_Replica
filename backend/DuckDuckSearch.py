from ddgs import DDGS
import requests
from bs4 import BeautifulSoup

def scrape_top_sites(query: str, max_sites: int = 5, chars_limit: int = 1000) -> str:
    """
    Search DuckDuckGo for a query and scrape text content from the top results.
    
    Parameters:
        query (str): Search term.
        max_sites (int): Number of top results to fetch. Default is 5.
        chars_limit (int): Max characters to extract from each page. Default is 1000.

    Returns:
        str: Concatenated summary of content from the top pages.
    """
    summaries = []

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_sites))

        for result in results:
            url = result.get("href") or result.get("url")
            if not url:
                continue

            try:
                response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(response.text, "html.parser")
                page_text = soup.get_text(separator=" ", strip=True)
                snippet = page_text[:chars_limit]
                summaries.append(f"From {url}:\n{snippet}")
            except Exception as e:
                summaries.append(f"Failed to load {url}: {str(e)}")
    except Exception as outer_e:
        return f"Search failed: {str(outer_e)}"

    return "\n\n".join(summaries)
