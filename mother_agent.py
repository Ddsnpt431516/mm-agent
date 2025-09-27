print("🕷️ मदर मायक्रो एजंट बिल्डर सुरू झाला आहे!")
print("==========================================")

def create_simple_agent():
    print("📝 नवीन एजंट तयार करण्यासाठी...")
    
    agent_name = input("एजंटचं नाव द्या: ")
    agent_type = input("एजंटचा प्रकार (data/api/chat): ")
    
    # साधा एजंट कोड तयार करतो
    agent_code = f'''
print("🌟 नमस्कार! मी {agent_name} एजंट आहे")
print("🔧 माझा प्रकार: {agent_type}")

def main():
    print("🚀 एजंट कार्यरत आहे...")
    # इथे भविष्यात काम जोडू शकता

if __name__ == "__main__":
    main()
'''
    
    # फाइल सेव्ह करण्यासाठी कोड
    filename = f"{agent_name}_agent.py"
    print(f"✅ {filename} तयार झाली!")
    print("\\n📄 एजंट कोड:")
    print(agent_code)
    
    return agent_code

# मुख्य मेनू
def main_menu():
    while True:
        print("\\n===== मदर एजंट बिल्डर =====")
        print("1. नवीन एजंट तयार करा")
        print("2. बिल्डर बद्दल माहिती")
        print("3. बाहेर पडा")
        
        choice = input("तुमची निवड द्या (1/2/3): ")
        
        if choice == "1":
            create_simple_agent()
        elif choice == "2":
            print("\\n📖 हा प्रोजेक्ट मायक्रो एजंट्स तयार करतो")
            print("💡 भविष्यात AI सह सुधारणा होईल")
        elif choice == "3":
            print("👋 धन्यवाद! पुन्हा भेटू")
            break
        else:
            print("❌ चुकीची निवड! पुन्हा प्रयत्न करा")

if __name__ == "__main__":
    main_menu()
