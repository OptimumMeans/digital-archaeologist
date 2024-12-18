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
    },
    {
        "title": "Early Computing",
        "artifact_name": "ENIAC",
        "year_of_origin": "1945",
        "description": "The first general-purpose electronic computer, weighing 30 tons.",
        "code_sample": "compute.ballistic_trajectory()",
        "fun_fact": "ENIAC's 18,000 vacuum tubes had to be replaced at a rate of several per day just to keep it running."
    },
    {
        "title": "Gaming History",
        "artifact_name": "Magnavox Odyssey",
        "year_of_origin": "1972",
        "description": "The first commercial home video game console.",
        "code_sample": "display.move_light_spot(x, y)",
        "fun_fact": "Players had to put plastic overlays on their TV screens to add color to the games."
    },
    {
        "title": "Personal Computing",
        "artifact_name": "Apple I",
        "year_of_origin": "1976",
        "description": "The first Apple computer, hand-built by Steve Wozniak.",
        "code_sample": "poke(memory_address, value)",
        "fun_fact": "The Apple I was priced at $666.66 because Wozniak liked repeating digits."
    },
    {
        "title": "Storage Evolution",
        "artifact_name": "IBM 350 RAMAC",
        "year_of_origin": "1956",
        "description": "The first commercial computer with a hard disk drive.",
        "code_sample": "seek_track(cylinder, head)",
        "fun_fact": "Its 5MB storage capacity cost $35,000 ($3,500 per MB) - today you can get a MB for a fraction of a cent."
    },
    {
        "title": "Networking Pioneers",
        "artifact_name": "TCP/IP Protocol",
        "year_of_origin": "1983",
        "description": "The fundamental communication protocol of the internet.",
        "code_sample": "packet.set_checksum(data)",
        "fun_fact": "The entire internet was shut down for a day to switch everyone to TCP/IP - known as 'Flag Day'."
    },
    {
        "title": "Computer Graphics",
        "artifact_name": "Utah Teapot",
        "year_of_origin": "1975",
        "description": "The most famous 3D test model in computer graphics.",
        "code_sample": "render.teapot(size, material)",
        "fun_fact": "This teapot has appeared in Toy Story, The Simpsons, and countless other works as an inside joke."
    },
    {
        "title": "Computer Mouse",
        "artifact_name": "First Mouse",
        "year_of_origin": "1964",
        "description": "The first computer mouse, invented by Doug Engelbart at SRI.",
        "code_sample": "cursor.move(delta_x, delta_y)",
        "fun_fact": "The first mouse was made of wood and had only one button."
    },
    {
        "title": "Early Programming",
        "artifact_name": "FORTRAN",
        "year_of_origin": "1957",
        "description": "The first widely used high-level programming language.",
        "code_sample": "DO 10 I = 1,N",
        "fun_fact": "FORTRAN reduced the number of programming statements necessary to operate a machine by a factor of 20."
    },
    {
        "title": "Operating Systems",
        "artifact_name": "UNIX",
        "year_of_origin": "1969",
        "description": "The operating system that revolutionized computing.",
        "code_sample": "fork(); exec();",
        "fun_fact": "UNIX's development started when Ken Thompson's wife was on vacation, giving him a month of free time."
    },
    {
        "title": "Computer Memory",
        "artifact_name": "Core Memory",
        "year_of_origin": "1951",
        "description": "The first reliable and commercially successful random access memory.",
        "code_sample": "memory.write(address, value)",
        "fun_fact": "Core memory was hand-woven by factory workers, mostly women, who were chosen for their fine motor skills."
    },
    {
        "title": "Game Consoles",
        "artifact_name": "Nintendo Game Boy",
        "year_of_origin": "1989",
        "description": "Revolutionary handheld gaming device that defined portable gaming.",
        "code_sample": "lcd.refresh_screen()",
        "fun_fact": "The Game Boy could run for 30 hours on four AA batteries, a major feat for its time."
    },
    {
        "title": "Computer Security",
        "artifact_name": "RSA Algorithm",
        "year_of_origin": "1977",
        "description": "The first public-key cryptosystem, fundamental to modern security.",
        "code_sample": "message = pow(ciphertext, private_key, n)",
        "fun_fact": "The 'S' in RSA stands for Shamir, who developed it at age 18."
    },
    {
        "title": "Computer Displays",
        "artifact_name": "Xerox Alto",
        "year_of_origin": "1973",
        "description": "First computer with a graphical user interface and bitmap display.",
        "code_sample": "window.draw_bitmap(x, y)",
        "fun_fact": "The Alto's display was oriented vertically (portrait), unlike today's landscape monitors."
    },
    {
        "title": "Microprocessors",
        "artifact_name": "Intel 4004",
        "year_of_origin": "1971",
        "description": "The first commercial microprocessor.",
        "code_sample": "cpu.execute_instruction()",
        "fun_fact": "The 4004 had 2,300 transistors and ran at 740 kHz - less power than a modern calculator."
    },
    {
        "title": "Data Storage",
        "artifact_name": "CompactFlash",
        "year_of_origin": "1994",
        "description": "One of the first successful solid-state storage formats.",
        "code_sample": "flash.write_sector(address)",
        "fun_fact": "The original CompactFlash cards used the same type of pin connection as IDE hard drives."
    },
    {
        "title": "Word Processing",
        "artifact_name": "WordPerfect",
        "year_of_origin": "1979",
        "description": "One of the first widely successful word processors.",
        "code_sample": "document.reveal_codes()",
        "fun_fact": "WordPerfect was originally written for a Data General minicomputer, not a PC."
    },
    {
        "title": "Computer Networks",
        "artifact_name": "Token Ring",
        "year_of_origin": "1984",
        "description": "IBM's pioneering local area network technology.",
        "code_sample": "token.pass_to_next()",
        "fun_fact": "Token Ring ran at 4 Mbps, four times faster than original Ethernet."
    },
    {
        "title": "Early AI",
        "artifact_name": "ELIZA",
        "year_of_origin": "1964",
        "description": "One of the first programs to process natural language.",
        "code_sample": "response = pattern.match(input)",
        "fun_fact": "ELIZA was named after Eliza Doolittle from 'Pygmalion', as both were taught to communicate better."
    },
    {
        "title": "Computer Sound",
        "artifact_name": "Sound Blaster",
        "year_of_origin": "1989",
        "description": "The sound card that set the standard for PC audio.",
        "code_sample": "audio.play_sample(frequency)",
        "fun_fact": "Sound Blaster became so popular that 'Sound Blaster compatible' became a standard requirement for sound cards."
    },
    {
        "title": "Digital Cameras",
        "artifact_name": "Kodak DCS 100",
        "year_of_origin": "1991",
        "description": "The first commercially available digital SLR camera.",
        "code_sample": "sensor.capture_image()",
        "fun_fact": "The DCS 100 used a modified Nikon F3 body and stored images on a separate hard drive unit."
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