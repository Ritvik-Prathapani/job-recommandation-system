import requests
import json

# Load skills from JSON file
with open("resume_data.json", "r") as f:
    skills_data = json.load(f)

skills = skills_data.get("skills", [])  # Assumes skills are stored under "skills" key
query = " ".join(skills)  # Combine skills into a search query

# JSearch API details
API_KEY = "1245",#give api key from rapid api(jsearch)
API_URL = "https://jsearch.p.rapidapi.com/search"

# API headers
headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# Request parameters
params = {
    "query": query,
    "page": 1,
    "num_pages": 1
}

# Make API request
response = requests.get(API_URL, headers=headers, params=params)

if response.status_code == 200:
    job_results = response.json().get("data", [])

    # Extract required job details
    jobs = [
        {
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "apply_link": job.get("job_apply_link")
        }
        for job in job_results
    ]

    # Save jobs to a JSON file
    with open("jobs.json", "w") as f:
        json.dump(jobs, f, indent=4)

    print("Jobs saved successfully to jobs.json")
else:
    print("Error fetching jobs:", response.text)
