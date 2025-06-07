# mcp-paperswithcode

[![smithery badge](https://smithery.ai/badge/@hbg/mcp-paperswithcode)](https://smithery.ai/server/@hbg/mcp-paperswithcode)

# 🦾 Features

> Allows AI assistants to find and read papers, as well as view related code repositories for further context.

This MCP server provides a Model Context Protocol (MCP) client that interfaces with the PapersWithCode API.

It includes tools for searching, retrieving, and parsing information on research papers, authors, datasets, conferences, and more.

# 🚀 Getting Started

### Installing via Smithery

To install mcp-paperswithcode for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@hbg/mcp-paperswithcode):

```bash
npx -y @smithery/cli install @hbg/mcp-paperswithcode --client claude
```

# 🛠️ Tools

## 📚 Paper Tools

### `search_papers`
Search for papers using optional filters.

- `abstract` (str, optional): Filter by abstract text.
- `title` (str, optional): Filter by title text.
- `arxiv_id` (str, optional): Filter by ArXiv ID.

### `get_paper`
Get a paper's metadata by its ID.

- `paper_id` (str): The paper ID.

### `read_paper_from_url`
Extract readable text from a paper given its URL.

- `paper_url` (str): The direct PDF or HTML URL to a paper.

### `list_paper_results`
List benchmark results associated with a paper.

- `paper_id` (str): The paper ID.

### `list_paper_tasks`
List tasks associated with a paper.

- `paper_id` (str): The paper ID.

### `list_paper_methods`
List methods discussed in a paper.

- `paper_id` (str): The paper ID.

### `list_paper_repositories`
List code repositories linked to a paper.

- `paper_id` (str): The paper ID.

### `list_paper_datasets`
List datasets mentioned or used in a paper.

- `paper_id` (str): The paper ID.

## 🧠 Research Area Tools

### `search_research_areas`
Search research areas by name.

- `name` (str): Partial or full name of the research area.

### `get_research_area`
Get metadata for a specific research area.

- `area_id` (str): The area ID.

### `list_research_area_tasks`
List tasks associated with a research area.

- `area_id` (str): The area ID.

## 👨‍🔬 Author Tools

### `search_authors`
Search authors by full name.

- `full_name` (str): Full name of the author.

### `get_paper_author`
Get metadata for an author by ID.

- `author_id` (str): The author ID.

### `list_papers_by_author_id`
List all papers written by an author via ID.

- `author_id` (str): The author ID.

### `list_papers_by_author_name`
Search by name and return papers for the first matching author.

- `author_name` (str): Full name of the author.

## 🎓 Conference Tools

### `list_conferences`
List conferences, optionally filter by name.

- `conference_name` (str, optional): Full or partial name.

### `get_conference`
Get metadata for a specific conference.

- `conference_id` (str): The conference ID.

### `list_conference_proceedings`
List all proceedings under a conference.

- `conference_id` (str): The conference ID.

### `get_conference_proceeding`
Get details for a specific conference proceeding.

- `conference_id` (str): The conference ID.
- `proceeding_id` (str): The proceeding ID.

### `list_conference_papers`
List all papers for a specific conference proceeding.

- `conference_id` (str): The conference ID.
- `proceeding_id` (str): The proceeding ID.
