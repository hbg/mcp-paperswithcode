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


@mcp.tool()
async def search_research_areas(
    name: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
    """Search for research areas that exist in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page,
        "name": name
    }
    url = f"{BASE_URL}/areas/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_research_area(area_id: str) -> dict:
    """Get a research area by ID in PapersWithCode"""
    url = f"{BASE_URL}/areas/{area_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_research_area_tasks(
    area_id: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
async def search_authors(
    full_name: str,
    page: int | None = 1,
    items_per_page: int | None = 20,
) -> dict:
    """Search for authors by name in PapersWithCode"""
    params = {
        "page": page,
        "items_per_page": items_per_page,
        "full_name": full_name,
    }
    url = f"{BASE_URL}/authors/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_paper_author(author_id: str) -> dict:
    """Get a paper author by ID in PapersWithCode"""
    url = f"{BASE_URL}/authors/{author_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_papers_by_author_id(
    author_id: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
    """List the papers written by a given author name in PapersWithCode"""
    # First search for the author
    authors_response = await search_authors(author_name)
    if not authors_response.get("results"):
        return {"count": 0, "next": None, "previous": None, "results": []}

    author_id = authors_response["results"][0]["id"]
    return await list_papers_by_author_id(author_id, page, items_per_page)


@mcp.tool()
async def list_conferences(
    conference_name: str | None = None,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
    """List the conferences in PapersWithCode"""
    params = {
        "name": conference_name,
        "page": page,
        "items_per_page": items_per_page
    }
    url = f"{BASE_URL}/conferences/?{encode_non_null_params(params)}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def get_conference(conference_id: str) -> dict:
    """Get a conference by ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_conference_proceedings(
    conference_id: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
async def get_conference_proceeding(conference_id: str, proceeding_id: str) -> dict:
    """Get a proceeding by ID in PapersWithCode"""
    url = f"{BASE_URL}/conferences/{conference_id}/proceedings/{proceeding_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_conference_papers(
    conference_id: str,
    proceeding_id: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    abstract: str | None = None,
    title: str | None = None,
    arxiv_id: str | None = None,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
async def get_paper(paper_id: str) -> dict:
    """Get a paper by ID in PapersWithCode"""
    url = f"{BASE_URL}/papers/{paper_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@mcp.tool()
async def list_paper_repositories(
    paper_id: str,
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
    page: int | None = 1,
    items_per_page: int | None = 20
) -> dict:
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
