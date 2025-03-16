"""Main MCP server for PapersWithCode"""
import io
from typing import Optional
from urllib.parse import urlencode
import httpx
import requests
from mcp.server.fastmcp import FastMCP
from PyPDF2 import PdfReader

mcp = FastMCP("Papers With Code MCP Interface")
BASE_URL = "https://paperswithcode.com/api/v1"


def encode_non_null_params(params):
    """Encode non-null URL parameters for the API"""
    if params:
        updated_params = {k: v for k, v in params.items() if v is not None}
        return urlencode(updated_params)
    return ""


@mcp.tool()
async def search_research_areas(
    query: Optional[str],
    name: Optional[str],
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """Search for research areas that exist in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page,
        "q": query,
        "name": name
    }
    url = f"{BASE_URL}/areas/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_research_area(area_id: str) -> str:
    """Get a research area by ID in PapersWithCode"""
    url = f"{BASE_URL}/areas/{area_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_research_area_tasks(
    area_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the tasks for a given research area ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page,
        "area": area_id
    }
    url = f"{BASE_URL}/tasks/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_authors(
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20,
    full_name: Optional[str] = None,
    query: Optional[str] = None
) -> str:
    """List the authors for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page,
        "full_name": full_name,
        "q": query
    }
    url = f"{BASE_URL}/authors/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_paper_author(author_id: str) -> str:
    """Get a paper author by ID in PapersWithCode"""
    url = f"{BASE_URL}/authors/{author_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_papers_by_author_id(
    author_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the papers for a given author ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/authors/{author_id}/papers/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_papers_by_author_name(
    author_name: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the papers written by a given author ID in PapersWithCode"""
    author_id = await get_paper_author(author_name)["id"]
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/authors/{author_id}/papers/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_conferences(
    conference_name: Optional[str] = None,
    q: Optional[str] = None,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the conferences in PapersWithCode"""
    params = {
        "name": conference_name,
        "q": q,
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/conferences/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_conference(conference_id: str) -> str:
    """Get a conference by ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_conference_proceedings(
    conference_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the proceedings for a given conference ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/conferences/{conference_id}/proceedings/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_conference_proceeding(proceeding_id: str) -> str:
    """Get a proceeding by ID in PapersWithCode"""
    url = f"{BASE_URL}/proceedings/{proceeding_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_conference_papers(
    conference_id: str,
    proceeding_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the papers for a given conference ID and proceeding ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    prefix = f"{BASE_URL}/conferences/{conference_id}/proceedings/{proceeding_id}/papers"
    url = f"{prefix}/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def search_papers(
    abstract: Optional[str] = None,
    title: Optional[str] = None,
    arxiv_id: Optional[str] = None,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """Search for a paper in PapersWithCode"""
    params = {
        "abstract": abstract,
        "title": title,
        "arxiv_id": arxiv_id,
        "page": page,
        "items_per_page": items_per_page
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/papers/?{encode_non_null_params(params)}")
        return response.json()


@mcp.tool()
async def get_paper(paper_id: str) -> str:
    """Get a paper by ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_repositories(
    paper_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the repositories for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/papers/{paper_id}/repositories/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_datasets(
    paper_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the datasets for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/papers/{paper_id}/datasets/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_methods(
    paper_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the methods for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/papers/{paper_id}/methods/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_results(
    paper_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the results for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/papers/{paper_id}/results/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_tasks(
    paper_id: str,
    page: Optional[int] = 1,
    items_per_page: Optional[int] = 20
) -> str:
    """List the tasks for a given paper ID in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/papers/{paper_id}/tasks/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def read_paper_from_url(paper_url: str) -> str:
    """Explain a paper by URL in PapersWithCode"""
    headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36' +\
                ' (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
    }
    response = requests.get(url=paper_url, headers=headers, timeout=120)
    content_io = io.BytesIO(response.content)
    pdf_file = PdfReader(content_io)
    count = len(pdf_file.pages)
    output = ""
    for i in range(count):
        page = pdf_file.pages[i]
        output += page.extract_text()
    return {
        "paper_content": output
    }

if __name__ == "__main__":
    mcp.run()
