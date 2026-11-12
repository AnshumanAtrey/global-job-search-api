# Job Search API - Greenhouse, Lever, Workday, Ashby & 14 More

Job search API for 18 job boards at once: type a job title and get the newest matching jobs from Hiring Cafe, Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Workable, Cornerstone, Deel, Y Combinator, Wellfound, Welcome to the Jungle (with Otta), eFinancialCareers, Naukri, foundit, Instahyre, Hirist and Cutshort, searched live and in parallel, each job once. Every row has the title, company, places, remote or office, job type, published pay, posting date, the board it came from and the apply link. Turn on full details for the description.

Use it as one multi job board scraper and API with no login and no API key, an ATS jobs API for company career sites, a job aggregator feed for your own job board, or a daily job alert, from the Apify Console, the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP, and export JSON, CSV or Excel. It is the alternative to running 18 job scrapers one after another: every board is searched at the same time, so a run takes about as long as its slowest board. Available as an [Apify Actor](https://apify.com/anshumanatrey/job-boards-search). $0.003 per job, $0.004 with full details, and $0.005 per board searched.

**Use it from an AI assistant:**

- **Claude** (claude.ai and the desktop app): [Add Job Boards Search to Claude](https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Job%20Boards%20Search&connectorUrl=https%3A%2F%2Fmcp.apify.com%3Ftools%3Danshumanatrey%2Fjob-boards-search), click Continue, sign in to Apify, Allow, and ask in plain words.
- **Claude Code:** `claude mcp add --transport http job-boards-search "https://mcp.apify.com?tools=anshumanatrey/job-boards-search"`, then run `/mcp` to sign in to Apify.
- **Codex:** `codex mcp add job-boards-search --url "https://mcp.apify.com?tools=anshumanatrey/job-boards-search"`, then `codex mcp login job-boards-search`.
- **Any other MCP client:** `https://mcp.apify.com?tools=anshumanatrey/job-boards-search`, signed in with Apify or an `Authorization: Bearer <APIFY_TOKEN>` header.

## What does it do?

- **Searches 18 job boards in one run, all at the same time.** Job boards that index jobs themselves (Hiring Cafe's 6 million jobs from employers' career sites, Y Combinator's Work at a Startup, Wellfound, Welcome to the Jungle and Otta, eFinancialCareers, and India's Naukri, foundit, Instahyre, Hirist and Cutshort) and company career sites on eight applicant tracking systems (Greenhouse's 8,357 job boards, Lever's 2,396, Workday's 2,207, Ashby's 3,814, SmartRecruiters' 2,917, Workable's 2,196, Cornerstone's 1,110 and Deel's 161).
- **The newest jobs of all of them, newest first.** Each board finds its newest matches, then the newest of them all are saved, up to Number of jobs (`maxJobs`), with the board each came from in `platform`.
- **Each job once.** A job listed on two boards (a company's Greenhouse posting that Hiring Cafe and eFinancialCareers also carry) is saved once: the same job link, the same company, title and city, or the same company and title posted at the same second.
- **The same filters on every board.** Job titles, places (cities, states, countries, regions, Worldwide), remote or office, job type, posting period, years of experience, words to leave out, and companies.
- **Links go to their own board.** A company link pasted in the search (job-boards.greenhouse.io/stripe) searches that board only; job links of any of the 18 boards are checked by their own board and come back open, closed or not found.
- **A summary per board.** The OUTPUT record says, for every board, how many jobs matched and were saved, how long it took, and any trouble it met.

## How is it different from other job search scrapers?

- **Job boards and company career sites together.** The multi-board actors on the Apify Store read applicant tracking systems or general job boards; this one reads both, India's job boards included, and keeps each job once across them.
- **Live at the moment of your run.** Every board is read when you run it, not from an index built earlier, so a job posted an hour ago can be in your results.
- **Titles that match.** A job matches when its title has every word of one of your lines, so 100 rows for data analyst are 100 data analyst jobs.
- **Parallel, with a time cap.** The boards are read at the same time, and Time per board (`secondsPerBoard`) caps how long any one of them searches: a slow board delivers what it found and the run goes on.
- **Open source.** The search engine behind it, one adapter per board, is public on GitHub under the MIT license.

## When should I use it?

- **Job seekers:** one search across every board for your title and city, newest first, each with its apply link.
- **Job boards and aggregators:** a fresh feed of jobs from career sites and job boards in one schema.
- **Recruiters and sales teams:** who is hiring for a role right now, and on which hiring system.
- **AI agents:** one tool that searches every board, instead of a tool per board.

## How much does it cost to search 18 job boards?

Pay per event: $3.00 per 1,000 jobs, or $4.00 per 1,000 with full details, plus $0.005 for each board a search reads, charged when the run starts. Apify's free $5 monthly credit covers about 12 runs of 100 jobs on all 18 boards, or about 28 runs of 50 jobs on 5 boards. Platform usage is included, and there is no monthly fee.

| Event | Price | When it is charged |
|---|---|---|
| Job | $0.003 | One saved job, and one checked job link that is closed or not found |
| Job with details | $0.004 | One saved job with full details on |
| Board searched | $0.005 | Once for each board a search reads, when the run starts (18 when every board is searched); checking job links charges none |

On Apify's paid plans a job costs less: $0.003 on BRONZE, $0.0027 on SILVER and $0.0024 on GOLD and above; a job with details $0.004, $0.0036 and $0.0032. The board fee is the same on every plan.

| Run | Cost |
|---|---|
| 100 jobs from all 18 boards | $0.39 |
| 50 jobs from 5 boards | $0.175 |
| 100 jobs from all 18 boards with full details | $0.49 |

Set a maximum cost per run in Apify and the run reads only the boards that fit, keeping room for at least one job, then stops saving at the limit.

## How does the price compare with other job search scrapers?

Every actor on the Apify Store that searches several job boards or applicant tracking systems in one run and had 80 or more users in the last 30 days on 2026-11-13, ordered by users. Prices are each actor's live price on Apify's free plan that day, with the run start at its default memory.

| Actor | Users, 30 days | What its description names | Per job | Start fee | 100 jobs |
|---|---|---|---|---|---|
| fantastic-jobs/career-site-job-listing-api | 1,607 | 275,000+ career sites on 58 ATS, AI enrichment | $0.012 | $0.01 | $1.21 |
| fantastic-jobs/career-site-job-listing-feed | 280 | The same career sites, as a feed | $0.0025 | $0.10 | $0.35 |
| agentx/all-jobs-scraper | 204 | 42 job platforms | $0.0035 | $0.01 | $0.36 |
| jobo.world/ats-jobs-api | 164 | 7 million jobs on 200+ ATS | $0.004 | $0.0002 | $0.40 |
| hirebase/job-search | 145 | 4 million jobs from Greenhouse, Workday, Lever and 20+ ATS | $0.005 | $0.004 | $0.50 |
| factpipe/ats-jobs-feed | 144 | 800,000 jobs on 8 ATS | $0.005 | none | $0.50 |
| yugenox/ats-jobs-search | 143 | Live search of 12,000 career sites on Greenhouse, Lever and Ashby | $0.002 | none | $0.20 |
| memo23/career-site-ats-jobs-api | 84 | 116 ATS, fetched at run time | $0.004 | $0.03 | $0.43 |
| bovi/greenhouse-lever-ashby-job-scraper | 80 | Greenhouse, Lever and Ashby, by company or preset list | $0.0015 | $0.00005 | $0.15 |
| jtpalms/ats-jobs-index | 80 | 17,000 career sites, indexed twice a day | $0.003 | $0.00005 | $0.30 |
| **This actor** | new | 18 boards: 10 job boards and 8 ATS, live | $0.003 | $0.005 a board | $0.39 (18 boards) |

Where others are cheaper: bovi, yugenox and jtpalms cost less for 100 jobs when Greenhouse, Lever and Ashby are all you need, and fantastic-jobs' feed and agentx cost a few cents less than a search of all 18 boards here. For one board, the matching actor below costs far less: Hiring Cafe Jobs Scraper charges $0.000062 a job. Where others do more: the database actors cover more applicant tracking systems (58 to 200+) and add AI-extracted fields.

## Which inputs does it take?

| Field | What it does |
|---|---|
| Job titles to find (`searchTerms`) | Job titles or keywords, one per line. A job matches when its title has every word of a line. Empty: the newest jobs of every kind. A pasted board link searches that board only |
| Job boards (`platforms`) | The boards to search, all at the same time. Empty: all 18. Keys or names (Hiring Cafe, YC, Otta) |
| Where the job is (`location`) | Cities, states, countries or regions; Worldwide; Remote alone asks for remote jobs |
| Remote or onsite (`workType`) | remote, hybrid or onsite |
| Posted in the last (`postedWithin`) | 24 hours, 3, 7, 14 or 30 days (the default), any time, or your own period |
| Number of jobs (`maxJobs`) | How many jobs in all, newest first across every board: 100 by default; 0 for every match |
| Full details (`includeDetails`) | Adds the description as text and HTML, pay as numbers and the address |
| Leave out words (`excludeTerms`) | Words that leave a job out when its title has them |
| Job type (`employmentType`) | full-time, part-time, contract, intern or temporary |
| Experience (`experienceYears`) | Your years: 3, 2-5, 5+ or fresher. Only boards that state years can match then |
| Match descriptions (`searchDescriptions`) | Matches your words in descriptions too; slower |
| Only these companies (`companies`) | Company names or board links; a board where none is found sits the run out |
| Job links to check (`jobUrls`) | Job links of any of the 18 boards to check instead of searching |
| Time per board (`secondsPerBoard`) | How long each board may search: 240 seconds by default; 0 for no cap of its own |

Example input:

```json
{
  "searchTerms": ["data analyst"],
  "location": ["London"],
  "platforms": ["hiringcafe", "greenhouse", "lever", "ashby", "efinancialcareers"],
  "postedWithin": "7 days",
  "maxJobs": 50
}
```

## What does the output look like?

One row per job, newest first across every board searched. A row from a search for data analyst in London on 2026-11-12:

```json
{
  "title": "EMEA | Senior Data Business Analyst / Product Owner (Contractor)",
  "company": "Infinite Lambda",
  "location": "London",
  "otherLocations": ["Romania", "Sofia I Bulgaria", "Hungary", "Spain", "Slovakia", "Portugal"],
  "workType": "remote",
  "employmentType": "full-time",
  "department": "Customer Success",
  "team": "Customer Success",
  "salary": null,
  "postedAt": "2026-11-11T10:52:26.238+00:00",
  "expiresAt": null,
  "jobUrl": "https://jobs.ashbyhq.com/Infinite%20Lambda/4bdf2b62-422f-4036-8645-cd1ffeef0a27",
  "applyUrl": "https://jobs.ashbyhq.com/Infinite%20Lambda/4bdf2b62-422f-4036-8645-cd1ffeef0a27/application",
  "status": "open",
  "platform": "ashby",
  "companySlug": "Infinite Lambda",
  "companyWebsite": "https://infinitelambda.com",
  "jobId": "4bdf2b62-422f-4036-8645-cd1ffeef0a27",
  "checkedAt": "2026-11-12T20:12:25+00:00"
}
```

| Field | What it holds |
|---|---|
| Job title (`title`) | The job title as the employer wrote it |
| Company name (`company`) | The company that is hiring |
| Main location (`location`), Other locations (`otherLocations`) | Every place the job names |
| Remote or onsite (`workType`) | remote, hybrid or onsite, when the job says |
| Job type (`employmentType`) | full-time, part-time, contract, intern or temporary, when the job says |
| Pay summary (`salary`) | Published pay as text; with full details also `salaryMin`, `salaryMax`, `salaryCurrency`, `salaryPeriod` |
| Posted on (`postedAt`) | When the job was posted |
| Job board (`platform`) | The board the row came from |
| Job link (`jobUrl`), Apply link (`applyUrl`) | The job on its board, and where to apply |
| Job description (`description`) | With full details: the description as text, and `descriptionHtml` |

Each board adds the fields its own actor gives, such as Hiring Cafe's `seniority`, `skills` and `visaSponsorship`, Y Combinator's `batch`, or Naukri's `experience`; the dataset schema names the boards that fill each field. The OUTPUT record holds the run summary: `boards` has one entry per board with `matchingJobs`, `jobsSaved`, `seconds`, `duplicatesOfOtherBoards` and any `boardsWithErrors`.

## How fast is it?

Minutes, because the boards are read at the same time. Measured on a laptop on 2026-11-13: software engineer on 16 boards (all but Ashby and Instahyre) took 255 s in one run, while the same search one board at a time adds up to 938 s. Data analyst in London on all 18 boards took 215 s: Greenhouse reads all of its 8,357 job boards (214 s), Lever and Ashby took under 3 minutes, and Hiring Cafe, Wellfound, Welcome to the Jungle and the India boards answered in 4 to 54 s. A run over all 18 boards peaked at 0.75 GB of memory.

## Common questions

### Which boards does it search?

All 18 unless you pick some in Job boards (`platforms`): hiringcafe, greenhouse, lever, workday, ashby, smartrecruiters, workable, cornerstone, deel, ycombinator, wellfound, welcometothejungle, efinancialcareers, naukri, foundit, instahyre, hirist and cutshort. Names work too: Hiring Cafe, YC, Otta, Monster India.

### Why does a run take a few minutes?

Company career sites have no search of their own across companies, so Greenhouse, Lever, Ashby and the other applicant tracking systems read every company's job list. The run takes about as long as its slowest board; lower Time per board (`secondsPerBoard`) to cap it, or pick the boards you need.

### How does it keep each job once?

A job is left out when a board earlier in the newest-first list already gave the same job link, the same company and title in the same city, or the same company and title posted at the same second. In a search for data analyst in London on all 18 boards (laptop, 2026-11-13), 24 jobs that two boards listed were saved once.

### Why did a board return nothing?

Its jobs may be older than the newest jobs of the other boards (raise Number of jobs), or it has none for your words and place: India's boards rarely list London jobs. The OUTPUT record's `boards` says what each board matched.

### Does it work on Apify's free plan?

Job Boards Search works on Apify's free plan, which pays $0.003 a job and $0.005 a board. The free $5 monthly credit pays for about 12 runs of 100 jobs on all 18 boards.

### How often should I run it?

Running Job Boards Search once a day keeps a job feed fresh: set Posted in the last (`postedWithin`) to 24 hours, schedule it under Schedules in Apify Console, and match rows on `jobUrl` to skip jobs you already have.

### How do I check a list of job links?

Paste them in Job links to check (`jobUrls`), one per line, from any of the 18 boards. Each goes to its own board and comes back open with the job, closed or not found, in the order pasted. A link of another site is skipped with a note.

### How do I call it from the API, Python, JavaScript, n8n or an AI agent?

Job Boards Search runs from the Apify API, Python, JavaScript, n8n, Make or an AI agent over MCP. Each way uses your Apify token (Apify Console, Settings, API & Integrations) and takes the input as JSON keyed by the field names, such as `searchTerms` and `platforms`.

**API.** One call runs the actor and returns its rows (Apify waits up to 300 seconds):

```bash
curl -X POST "https://api.apify.com/v2/acts/anshumanatrey~job-boards-search/run-sync-get-dataset-items" \
  -H "Authorization: Bearer <YOUR_APIFY_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"searchTerms": ["data analyst"], "location": ["London"], "platforms": ["hiringcafe", "greenhouse", "ashby"]}'
```

**Python** (`pip install apify-client`):

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_APIFY_TOKEN>")
run = client.actor("anshumanatrey/job-boards-search").call(run_input={"searchTerms": ["data analyst"]})
for row in client.dataset(run.default_dataset_id).iterate_items():  # apify-client 3+; on 2.x use run["defaultDatasetId"]
    print(row["platform"], row["title"], row["company"], row["location"], row["applyUrl"])
```

**JavaScript** (`npm install apify-client`):

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: '<YOUR_APIFY_TOKEN>' });
const run = await client.actor('anshumanatrey/job-boards-search').call({ searchTerms: ['data analyst'] });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.platform, row.title, row.company, row.location, row.applyUrl);
```

**n8n and Make.** In n8n, add the Apify node, pick Run an Actor and get dataset, choose this actor and paste the input JSON. In Make, the Apify app's Run an Actor and Get Dataset Items modules do the same.

**AI agents (MCP).** Add `https://mcp.apify.com?tools=anshumanatrey/job-boards-search` to your MCP client and sign in with Apify, or send `Authorization: Bearer <YOUR_APIFY_TOKEN>`. The agent gets one tool that searches all 18 boards and sees every input field by its JSON key.

### Is it legal to use?

Job Boards Search reads public job postings, the pages any visitor sees without logging in. It is not affiliated with any of the boards it reads. You are responsible for how you use the data, including each board's terms and the privacy laws that apply to you.

## Limitations

- A run takes about as long as its slowest board, up to Time per board (`secondsPerBoard`, 240 seconds by default); a board stopped there delivers what it found, and the OUTPUT record says so.
- Experience (`experienceYears`) keeps only jobs that state years: company career sites state none, so with it set only Hiring Cafe, Y Combinator, Wellfound, Welcome to the Jungle and the India boards can match.
- Each board keeps the limits of its own actor: Workable's jobs feed can end before today's jobs, Instahyre reads its jobs one by one, and HiringCafe shows a search's newest 10,000 employers.
- Pay is published on part of the jobs only, and `salary` is empty for the rest.
- Places are matched as each board writes them, so a US city next to United States finds more.
- Two listings of one job written differently on two boards (another title, another city) can both be saved.

## Who maintains it?

Built and maintained by **Anshuman Atrey** ([@AnshumanAtrey](https://github.com/AnshumanAtrey)), who publishes a portfolio of data and OSINT actors on Apify Store. For a feature request or a bug, message [LinkedIn](https://linkedin.com/in/anshumanatrey) (fastest), open an issue on the GitHub repo, or write through [atrey.dev](https://atrey.dev).

## Sibling actors

One board at a time, for less:

| Actor | What it searches |
|---|---|
| [Hiring Cafe Jobs Scraper](https://apify.com/anshumanatrey/hiringcafe-jobs-search) | HiringCafe's 6 million jobs from employers' own career sites |
| [Greenhouse Jobs Scraper](https://apify.com/anshumanatrey/greenhouse-jobs-search) | Jobs from every company on Greenhouse |
| [Lever Jobs Scraper](https://apify.com/anshumanatrey/lever-jobs-search) | Jobs from 2,300+ companies on Lever |
| [Workday Jobs Scraper](https://apify.com/anshumanatrey/workday-job-search) | Jobs from every company on Workday |
| [Ashby Jobs Scraper](https://apify.com/anshumanatrey/ashby-jobs-search) | Jobs from every company on Ashby |
| [SmartRecruiters Jobs Scraper](https://apify.com/anshumanatrey/smartrecruiters-jobs-search) | Jobs from 2,900+ companies on SmartRecruiters |
| [Workable Jobs Scraper](https://apify.com/anshumanatrey/workable-job-search) | Jobs from every company on Workable |
| [Cornerstone Jobs Scraper](https://apify.com/anshumanatrey/cornerstone-jobs-search) | Jobs from every company on Cornerstone |
| [Deel Jobs Scraper](https://apify.com/anshumanatrey/deel-jobs-search) | Jobs from every company on Deel ATS, with pay |
| [Y Combinator Jobs Scraper](https://apify.com/anshumanatrey/ycombinator-jobs-search) | YC startup jobs from Work at a Startup |
| [Wellfound Jobs Scraper](https://apify.com/anshumanatrey/wellfound-jobs-search) | Startup jobs on Wellfound |
| [Welcome to the Jungle Jobs Scraper](https://apify.com/anshumanatrey/welcome-to-the-jungle-jobs-search) | Welcome to the Jungle and Otta jobs |
| [eFinancialCareers Jobs Scraper](https://apify.com/anshumanatrey/efinancialcareers-jobs-search) | Finance, banking and quant jobs |
| [Naukri Jobs Scraper](https://apify.com/anshumanatrey/naukri-jobs-search) | India's biggest job board |
| [Foundit Jobs Scraper](https://apify.com/anshumanatrey/foundit-jobs-search) | foundit (Monster India) in 9 countries |
| [Instahyre Jobs Scraper](https://apify.com/anshumanatrey/instahyre-jobs-search) | Tech jobs on Instahyre |
| [Hirist Jobs Scraper](https://apify.com/anshumanatrey/hirist-jobs-search) | Tech jobs on Hirist |
| [Cutshort Jobs Scraper](https://apify.com/anshumanatrey/cutshort-jobs-search) | Startup jobs on Cutshort |

## Documentation

- Apify Store: https://apify.com/anshumanatrey/job-boards-search
- GitHub repo: https://github.com/AnshumanAtrey/job-boards-search (MIT license, see [LICENSE](LICENSE))
- The engine behind it: https://github.com/AnshumanAtrey/ats-jobs-engine

## Last updated

2026-11-13 (version 1.0)
