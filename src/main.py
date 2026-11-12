"""Job Boards Search: the shared job engine (github.com/AnshumanAtrey/ats-jobs-engine) on 18 job boards at once."""
import asyncio

from ats_jobs.many import main_many

if __name__ == '__main__':
    asyncio.run(main_many('job-boards-search'))
