# mcp-paperswithcode

[![smithery badge](https://smithery.ai/badge/@hbg/mcp-paperswithcode)](https://smithery.ai/server/@hbg/mcp-paperswithcode)

# Description

This repository provides an Model Context Protocol (MCP) client that can interface with the PapersWithCode API. Specifically, these MCP tools provide the API's abilities to get authors, papers, conferences, repositories, methods, results and tasks.

Additionally, helper tools are introduced to make it easier for the AI agent to make use of the information provided through the PapersWithCode API.

# Tools

- `list_paper_results(paper_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Lists the results for a given paper ID in PapersWithCode, allowing pagination through the `page` and `items_per_page` parameters.

- `list_paper_tasks(paper_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Retrieves the tasks associated with a specific paper ID in PapersWithCode, with options for pagination.

- `explain_paper(paper_url: str)`: Provides an explanation of a paper by its URL in PapersWithCode. It fetches the paper content and extracts text from the PDF for analysis.

- `list_paper_methods(paper_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Lists the methods related to a given paper ID in PapersWithCode, supporting pagination.

- `list_paper_authors(paper_id: str)`: Retrieves the authors of a specific paper ID in PapersWithCode.

- `list_paper_conferences(paper_id: str)`: Lists the conferences associated with a given paper ID in PapersWithCode.

- `list_paper_repositories(paper_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Retrieves the repositories linked to a specific paper ID in PapersWithCode.

- `search_research_areas(query: Optional[str], name: Optional[str], page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Search for research areas that exist in PapersWithCode with optional filtering by query or name.

- `get_research_area(area_id: str)`: Get detailed information about a specific research area by ID.

- `list_research_area_tasks(area_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List the tasks for a given research area ID in PapersWithCode.

- `list_paper_authors(page: Optional[int] = 1, items_per_page: Optional[int] = 20, full_name: Optional[str] = None, query: Optional[str] = None)`: List authors with optional filtering by name or query.

- `get_paper_author(author_id: str)`: Get detailed information about a specific author by ID.

- `list_papers_by_author_id(author_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List papers written by a specific author using their ID.

- `list_papers_by_author_name(author_name: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List papers written by an author using their name.

- `list_conferences(conference_name: Optional[str] = None, q: Optional[str] = None, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List conferences with optional filtering by name or query.

- `get_conference(conference_id: str)`: Get detailed information about a specific conference by ID.

- `list_conference_proceedings(conference_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List proceedings for a given conference.

- `get_conference_proceeding(proceeding_id: str)`: Get detailed information about a specific conference proceeding.

- `list_conference_papers(conference_id: str, proceeding_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List papers presented at a specific conference proceeding.

- `search_papers(abstract: Optional[str] = None, title: Optional[str] = None, arxiv_id: Optional[str] = None, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: Search for papers with optional filtering by abstract, title, arxiv ID, or general query.

- `get_paper(paper_id: str)`: Get detailed information about a specific paper by ID.

- `list_paper_datasets(paper_id: str, page: Optional[int] = 1, items_per_page: Optional[int] = 20)`: List datasets used or referenced in a specific paper.

# Example Usage

## Claude

## Cursor

### Installing via Smithery

To install mcp-paperswithcode for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@hbg/mcp-paperswithcode):

```bash
npx -y @smithery/cli install @hbg/mcp-paperswithcode --client claude
```y @smithery/cli@latest run @hbg/mcp-paperswithcode --config "{}"
```
