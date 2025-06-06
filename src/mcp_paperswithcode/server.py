"""Main MCP server for PapersWithCode"""
import io
from urllib.parse import urlencode
import httpx
import requests
from mcp.server.fastmcp import FastMCP
from PyPDF2 import PdfReader

mcp = FastMCP("Papers With Code MCP Interface")
BASE_URL = "https://paperswithcode.com/api/v1"

def encode_non_null_params(params: dict) -> str:
    """Encode non-null URL parameters for the API"""
    if params:
        updated_params = {k: v for k, v in params.items() if v is not None}
        return urlencode(updated_params)
    return ""

async def get_all_results(url: str) -> list:
    """Helper function to fetch all paginated results from a PapersWithCode endpoint"""
    all_results = []
    while url:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            all_results.extend(data.get("results", []))
            url = data.get("next")
    return all_results

@mcp.tool()
async def search_research_areas(name: str) -> dict:
    """Search for research areas that exist in PapersWithCode"""
    params = {"name": name}
    url = f"{BASE_URL}/areas/?{encode_non_null_params(params)}"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def get_research_area(area_id: str) -> dict:
    """Get a research area by ID in PapersWithCode"""
    url = f"{BASE_URL}/areas/{area_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@mcp.tool()
async def list_research_area_tasks(area_id: str) -> dict:
    """List the tasks for a given research area ID in PapersWithCode"""
    params = {"area": area_id}
    url = f"{BASE_URL}/tasks/?{encode_non_null_params(params)}"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def search_authors(full_name: str) -> dict:
    """Search for authors by name in PapersWithCode"""
    params = {"full_name": full_name}
    url = f"{BASE_URL}/authors/?{encode_non_null_params(params)}"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def get_paper_author(author_id: str) -> dict:
    """Get a paper author by ID in PapersWithCode"""
    url = f"{BASE_URL}/authors/{author_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@mcp.tool()
async def list_papers_by_author_id(author_id: str) -> dict:
    """List the papers for a given author ID in PapersWithCode"""
    url = f"{BASE_URL}/authors/{author_id}/papers/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def list_papers_by_author_name(author_name: str) -> dict:
    """List the papers written by a given author name in PapersWithCode"""
    authors_response = await search_authors(author_name)
    if not authors_response.get("results"):
        return {"results": []}
    author_id = authors_response["results"][0]["id"]
    return await list_papers_by_author_id(author_id)

@mcp.tool()
async def list_conferences(conference_name: str | None = None) -> dict:
    """List the conferences in PapersWithCode"""
    params = {"name": conference_name}
    url = f"{BASE_URL}/conferences/?{encode_non_null_params(params)}"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def get_conference(conference_id: str) -> dict:
    """Get a conference by ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@mcp.tool()
async def list_conference_proceedings(conference_id: str) -> dict:
    """List the proceedings for a given conference ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/proceedings/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def get_conference_proceeding(conference_id: str, proceeding_id: str) -> dict:
    """Get a proceeding by ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/proceedings/{proceeding_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@mcp.tool()
async def list_conference_papers(conference_id: str, proceeding_id: str) -> dict:
    """List the papers for a given conference ID and proceeding ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/proceedings/{proceeding_id}/papers/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def search_papers(abstract: str | None = None, title: str | None = None, arxiv_id: str | None = None) -> dict:
    """Search for a paper in PapersWithCode"""
    params = {"abstract": abstract, "title": title, "arxiv_id": arxiv_id}
    url = f"{BASE_URL}/papers/?{encode_non_null_params(params)}"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def get_paper(paper_id: str) -> dict:
    """Get a paper by ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@mcp.tool()
async def list_paper_repositories(paper_id: str) -> dict:
    """List the repositories for a given paper ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/repositories/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def list_paper_datasets(paper_id: str) -> dict:
    """List the datasets for a given paper ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/datasets/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def list_paper_methods(paper_id: str) -> dict:
    """List the methods for a given paper ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/methods/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def list_paper_results(paper_id: str) -> dict:
    """List the results for a given paper ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/results/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def list_paper_tasks(paper_id: str) -> dict:
    """List the tasks for a given paper ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/tasks/"
    results = await get_all_results(url)
    return {"results": results}

@mcp.tool()
async def read_paper_from_url(paper_url: str) -> dict:
    """Explain a paper by URL in PapersWithCode"""
    try:
        response = requests.get(paper_url)
        if response.headers.get('content-type') == 'application/pdf':
            pdf_content = io.BytesIO(response.content)
            reader = PdfReader(pdf_content)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return {"text": text, "type": "pdf"}
        else:
            return {"text": response.text, "type": "html"}
    except Exception as e:
        return {"error": str(e), "type": "error"}

if __name__ == "__main__":
    mcp.run()
