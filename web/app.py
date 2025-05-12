from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from agent.agent import agent
from agents import Runner
import asyncio

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@socketio.on("start_agent")
def start_agent(data):
    field          = data.get("field", "")
    summary_points = data.get("summary_points", "")
    style          = data.get("style", "")

    # Build the single prompt
    prompt = (
        f"field={field};"
        f"summary_points={summary_points};"
        f"style={style}"
    )

    # Spawn a fresh event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def _run():
        emit("log", {"message": "🧠 Agent starting..."})
        try:
            # Runner.run will call your write_file tool at the end
            result = await Runner.run(agent, prompt)
            
            # Agent's final_output should be the filesystem path from write_file
            file_path = result.final_output.strip()
            emit("log", {"message": f"✅ Agent finished. File written to: {file_path}"})

            # Optionally, read it back and send the MDX contents to the UI
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    mdx = f.read()
                emit("result", {"markdown": mdx, "file": file_path})
            except Exception:
                emit("result", {"markdown": "", "file": file_path})
        except Exception as e:
            emit("log", {"message": f"❌ Error during agent run: {e}"})

    loop.run_until_complete(_run())

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
