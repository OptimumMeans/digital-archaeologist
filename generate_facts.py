import json
from datetime import datetime
import random

# Expanded themed artifacts database
TECH_ARTIFACTS = [
    {
        "title": "AI Milestones",
        "artifact_name": "IBM Deep Blue",
        "year_of_origin": "1997",
        "description": "The first computer to defeat a reigning world chess champion.",
        "code_sample": "if (position.evaluate() > bestMove.score) { bestMove = position; }",
        "fun_fact": "Deep Blue could evaluate 200 million positions per second."
    },
    {
        "title": "Robotics Evolution",
        "artifact_name": "Boston Dynamics Atlas",
        "year_of_origin": "2013",
        "description": "First humanoid robot capable of dynamic movement and parkour.",
        "code_sample": "balance.adjust(sensor_data.gyroscope)",
        "fun_fact": "Atlas can perform backflips and recover from pushes while walking."
    },
    {
        "title": "Drone Innovation",
        "artifact_name": "Predator Drone",
        "year_of_origin": "1995",
        "description": "Pioneer of modern unmanned aerial surveillance.",
        "code_sample": "altitude.maintain(operation_ceiling)",
        "fun_fact": "The Predator can stay airborne for over 40 hours continuously."
    },
    {
        "title": "Computing Breakthroughs",
        "artifact_name": "Quantum Supremacy",
        "year_of_origin": "2019",
        "description": "Google's Sycamore processor performed a calculation in 200 seconds that would take classical computers 10,000 years.",
        "code_sample": "qubit.superposition(state_1, state_2)",
        "fun_fact": "Quantum computers use qubits that can be both 0 and 1 simultaneously."
    },
    {
        "title": "AI Evolution",
        "artifact_name": "GPT-3",
        "year_of_origin": "2020",
        "description": "OpenAI's large language model capable of generating human-like text.",
        "code_sample": "response = model.generate(prompt, max_tokens=100)",
        "fun_fact": "GPT-3 has 175 billion parameters, making it one of the largest neural networks ever created."
    },
    {
        "title": "Internet History",
        "artifact_name": "ARPANET",
        "year_of_origin": "1969",
        "description": "The first operational packet-switching network, predecessor to the internet.",
        "code_sample": "packet.route(source_node, destination_node)",
        "fun_fact": "The first ARPANET message crashed after sending just 'LO' - attempting to send 'LOGIN'."
    },
    {
        "title": "Robotics Pioneers",
        "artifact_name": "Unimate",
        "year_of_origin": "1961",
        "description": "The first industrial robot arm, revolutionizing manufacturing.",
        "code_sample": "arm.move_to(target_position)",
        "fun_fact": "Unimate was first used by General Motors to handle hot die-cast metal."
    },
    {
        "title": "Space Technology",
        "artifact_name": "Voyager 1",
        "year_of_origin": "1977",
        "description": "The first human-made object to enter interstellar space.",
        "code_sample": "signal.transmit(earth_coordinates)",
        "fun_fact": "Voyager 1's computer has only 69.63 kilobytes of memory, less than an average email."
    },
    {
        "title": "Mobile Revolution",
        "artifact_name": "iPhone",
        "year_of_origin": "2007",
        "description": "The first smartphone to feature a revolutionary multi-touch interface.",
        "code_sample": "touchscreen.detectMultiTouch(event)",
        "fun_fact": "The original iPhone had less processing power than a modern car key."
    },
    {
        "title": "Virtual Reality",
        "artifact_name": "Oculus Rift",
        "year_of_origin": "2012",
        "description": "The headset that sparked the modern VR revolution.",
        "code_sample": "vr.renderStereoView(left_eye, right_eye)",
        "fun_fact": "The Oculus Rift started as a Kickstarter project raising $2.4 million."
    },
    {
        "title": "AI Games",
        "artifact_name": "AlphaGo",
        "year_of_origin": "2016",
        "description": "First AI to defeat a professional Go player.",
        "code_sample": "move = self.policy_network.predict(board_state)",
        "fun_fact": "There are more possible Go positions than atoms in the universe."
    },
    {
        "title": "Computer Vision",
        "artifact_name": "LeNet-5",
        "year_of_origin": "1998",
        "description": "Pioneering convolutional neural network for digit recognition.",
        "code_sample": "conv_layer = Conv2D(filters=6, kernel_size=5)",
        "fun_fact": "LeNet-5 could process handwritten digits with 99.2% accuracy."
    },
    {
        "title": "Quantum Computing",
        "artifact_name": "IBM Q System One",
        "year_of_origin": "2019",
        "description": "First commercial quantum computer.",
        "code_sample": "quantum_circuit.h(qubit[0])",
        "fun_fact": "The Q System One must be cooled to near absolute zero to function."
    },
    {
        "title": "Autonomous Vehicles",
        "artifact_name": "Stanford Cart",
        "year_of_origin": "1979",
        "description": "One of the first self-driving vehicles.",
        "code_sample": "vision.detect_obstacles(camera_feed)",
        "fun_fact": "The Cart took 15 minutes to move one meter while avoiding obstacles."
    },
    {
        "title": "Cloud Computing",
        "artifact_name": "AWS S3",
        "year_of_origin": "2006",
        "description": "Revolutionary object storage service that shaped cloud computing.",
        "code_sample": "s3.upload_file(file_name, bucket)",
        "fun_fact": "S3 stored over 100 trillion objects by 2021."
    }
]

def get_unique_artifact():
    """Generate a unique artifact with current date and sequential number."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Read existing artifacts to ensure uniqueness
    try:
        with open("previous_artifacts.json", "r") as f:
            previous_artifacts = json.load(f)
    except FileNotFoundError:
        previous_artifacts = []
    
    # Get artifact numbers already used
    used_numbers = {int(a["artifact_number"]) for a in previous_artifacts}
    
    # Find next available number
    artifact_number = 1
    while artifact_number in used_numbers:
        artifact_number += 1
    
    # Select random artifact and add metadata
    artifact = random.choice(TECH_ARTIFACTS).copy()
    artifact.update({
        "date": current_date,
        "artifact_number": f"{artifact_number:03}"
    })
    
    # Save updated list
    previous_artifacts.append(artifact)
    with open("previous_artifacts.json", "w") as f:
        json.dump(previous_artifacts, f, indent=2)
    
    return artifact

def get_current_artifact():
    """Get the current artifact for the TRMNL display."""
    artifact = get_unique_artifact()
    
    return {
        "year": artifact["year_of_origin"],
        "title": artifact["artifact_name"],
        "description": artifact["description"],
        "fun_fact": artifact["fun_fact"],
        "artifact_number": artifact["artifact_number"]
    }

if __name__ == "__main__":
    print(json.dumps(get_current_artifact(), indent=2))