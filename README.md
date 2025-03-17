# mcp-paperswithcode

[![smithery badge](https://smithery.ai/badge/@hbg/mcp-paperswithcode)](https://smithery.ai/server/@hbg/mcp-paperswithcode)

# 🦾 Features

> Allows AI assistants to find and read papers, as well as view related code repositories for further context.

This MCP server provides an Model Context Protocol (MCP) client that can interface with the PapersWithCode API.

Additionally, helper tools are introduced to make it easier for the AI agent to make use of the information provided through the PapersWithCode API.

# 🚀 Getting Started

### Installing via Smithery

To install mcp-paperswithcode for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@hbg/mcp-paperswithcode):

```bash
npx -y @smithery/cli install @hbg/mcp-paperswithcode --client claude
```

# Tools

## Paper Search and Retrieval

1. **Search Papers**

   Search for papers with optional filtering by abstract, title, arxiv ID:

   ```python
   result = await search_papers(
       abstract="neural networks",
       title="attention mechanism",
       arxiv_id=None,
       page=1,
       items_per_page=20
   )
   ```

2. **Get Paper**

   Get detailed information about a specific paper by ID:

   ```python
   result = await get_paper(
       paper_id="paper123"
   )
   ```

3. **Read Paper From URL**

   Extract and read the content of a paper from its URL:

   ```python
   result = await read_paper_from_url(
       paper_url="https://arxiv.org/pdf/1706.03762.pdf"
   )
   ```

## Paper Components

1. **List Paper Results**

   Lists the results for a given paper ID in PapersWithCode:

   ```python
   result = await list_paper_results(
       paper_id="paper123",
       page=1,
       items_per_page=20
   )
   ```

2. **List Paper Tasks**

   Retrieves the tasks associated with a specific paper ID:

   ```python
   result = await list_paper_tasks(
       paper_id="paper123",
       page=1,
       items_per_page=20
   )
   ```

3. **List Paper Methods**

   Lists the methods related to a given paper ID:

   ```python
   result = await list_paper_methods(
       paper_id="paper123",
       page=1,
       items_per_page=20
   )
   ```

4. **List Paper Repositories**

   Retrieves the repositories linked to a specific paper ID:

   ```python
   result = await list_paper_repositories(
       paper_id="paper123",
       page=1,
       items_per_page=20
   )
   ```

5. **List Paper Datasets**

   List datasets used or referenced in a specific paper:

   ```python
   result = await list_paper_datasets(
       paper_id="paper123",
       page=1,
       items_per_page=20
   )
   ```

## Research Areas

1. **Search Research Areas**

   Search for research areas that exist in PapersWithCode:

   ```python
   result = await search_research_areas(
       name="computer vision",
       page=1,
       items_per_page=20
   )
   ```

2. **Get Research Area**

   Get detailed information about a specific research area by ID:

   ```python
   result = await get_research_area(
       area_id="area123"
   )
   ```

3. **List Research Area Tasks**

   List the tasks for a given research area ID:

   ```python
   result = await list_research_area_tasks(
       area_id="area123",
       page=1,
       items_per_page=20
   )
   ```

## Authors

1. **Get Paper Author**

   Get authors matching a full name:

   ```python
   result = await get_paper_author(
       full_name="Geoffrey Hinton",
       page=1,
       items_per_page=20
   )
   ```

2. **List Papers by Author ID**

   List papers written by a specific author using their ID:

   ```python
   result = await list_papers_by_author_id(
       author_id="author123",
       page=1,
       items_per_page=20
   )
   ```

## Conferences

1. **List Conferences**

   List conferences with optional filtering by name:

   ```python
   result = await list_conferences(
       conference_name="NeurIPS",
       page=1,
       items_per_page=20
   )
   ```

2. **Get Conference**

   Get detailed information about a specific conference by ID:

   ```python
   result = await get_conference(
       conference_id="conf123"
   )
   ```

3. **List Conference Proceedings**

   List proceedings for a given conference:

   ```python
   result = await list_conference_proceedings(
       conference_id="conf123",
       page=1,
       items_per_page=20
   )
   ```

4. **Get Conference Proceeding**

   Get detailed information about a specific conference proceeding:

   ```python
   result = await get_conference_proceeding(
       conference_id="conf123",
       proceeding_id="proc123"
   )
   ```

5. **List Conference Papers**

   List papers presented at a specific conference proceeding:

   ```python
   result = await list_conference_papers(
       conference_id="conf123",
       proceeding_id="proc123",
       page=1,
       items_per_page=20
   )
   ```

