# 🧠 Research Blogger AI Agent

<p align="center">
  <img src="research-blogger-agent.png" alt="Research Blogger Agent" width="400"/>
</p>

A fully automated AI-powered agent that:

1. **Fetches** the latest research paper from ArXiv based on a user-specified field.
2. **Summarizes** the paper's key points (methods, results, limitations).
3. **Drafts** a styled blog post in MDX format.
4. **Pushes** the generated MDX file to a specified GitHub repository for automatic deployment via Docusaurus.

This project uses the **OpenAI Agents SDK** to dynamically generate content from academic papers. The **Flask web app** serves as a control and monitoring panel. Additionally, the agent can run independently via a CLI, and GitHub Actions are utilized as a serverless function to execute the agent periodically.



## 🚀 Features

* **Dynamic Paper Selection**: Pulls the most recent papers from ArXiv and randomly selects one to avoid repetition.
* **AI Summarization**: Uses OpenAI's GPT-4o model to generate clear, concise summaries.
* **Blog Post Generation**: Produces a well-structured, customizable-length blog post in MDX format.
* **Custom Styles**: Supports various writing styles such as conversational, formal, analytical, and more.
* **GitHub Integration**: Pushes generated blog posts to the specified GitHub repository for automatic deployment.
* **Serverless Execution with GitHub Actions**: Runs the agent periodically without requiring a dedicated server.
* **Interactive Web UI**: Easy-to-use control panel for starting the agent and viewing logs.



## 📂 Project Structure

```
research-blogger-agent/
├── agent/
│   └── research_agent.py      # Core logic: fetch, summarize, write, push.
├── web/
│   ├── templates/
│   │   └── index.html         # Frontend form & display
│   ├── app.py                 # Flask control panel
│   └── requirements.txt       # Python dependencies
├── Dockerfile
├── docker-compose.yml
├── .env                       # API keys and repo info
├── GitHub Actions/            # Serverless function configuration
└── README.md                  # This file
```



## 📝 Prerequisites

* **Docker** & **Docker Compose**
* **OpenAI API key** (add to `.env` as `OPENAI_API_KEY`)
* **GitHub Personal Access Token** (add to `.env` as `GITHUB_TOKEN`)
* **GitHub Repository** for blog deployment via Docusaurus.



## 🌟 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/kl1d/research-agent.git
   cd research-blogger-agent
   ```

2. **Create a `.env` file**

   ```bash
   OPENAI_API_KEY=sk-...
   GITHUB_TOKEN=ghp-...
   BLOG_REPO=username/repo
   BLOG_PATH=blog
   ```

3. **Build & Run**

   ```bash
   docker-compose up --build
   ```

4. **Access the UI**
   Open your browser and go to `http://localhost:5005/`.



## 💻 Usage via Flask UI

1. Enter the **Research Field** (e.g., `cyber deception`).
2. Specify **Summary Points** (e.g., `methods, results, limitations`).
3. Choose a **Writing Style** (e.g., `conversational, 800 words`).
4. Click **Run Agent** and see the blog post generated in the UI.



## 💻 Running the Agent Directly (CLI)

You can also invoke the agent directly without the web UI:

```bash
docker exec -it agent python3 -m agent.agent \
   --field "cybersecurity" \
   --summary_points "methods, results" \
   --style "conversational, 400 words"
```

This will output the generated blog post and its GitHub link directly to the console.



## 🌐 GitHub Integration

* The agent pushes the generated MDX file to the specified GitHub repository under the given path.
* Ensure the GitHub token has **repo** permissions to push changes.

### Handling Issues:

* **Filename Extension Issue**: The agent now ensures that all files end with `.mdx`.
* **Commit Conflicts**: The agent handles updating existing files seamlessly.



## 🕒 Automated Execution with GitHub Actions

The agent is configured to run periodically (e.g., twice a week) as a serverless function using **GitHub Actions**. This setup allows the agent to continuously fetch new research papers, generate summaries, and push them to GitHub without manual intervention.

### Approach:

1. Use the Docker container directly in the GitHub Actions workflow.
2. Cache dependencies to reduce setup time.
3. Specify the field, summary points, style, and length as part of the CLI command.
4. Run the agent once, wait for the task to complete, and shut down.



## 🚧 Future Enhancements

* **Full Paper Summarization**: Moving beyond abstracts to include full paper content.
* **Adaptive Scheduling**: Adjusting fetching frequency based on recent paper activity.
* **User-defined Tagging**: Enhancing flexibility in how tags are generated and formatted.



## 🤝 Contributing

Pull requests are welcome! Please open an issue or PR with your ideas and improvements.



## 📄 License

This project is licensed under the MIT License.
