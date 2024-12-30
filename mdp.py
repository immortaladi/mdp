def display_awareness():
    print("🌳 Welcome to Forest and Wildlife Awareness Program 🌿")
    print("-" * 50)
    print("1. Importance of Forests")
    print("2. Importance of Wildlife")
    print("3. Ways to Conserve Forests")
    print("4. Ways to Conserve Wildlife")
    print("5. Exit")
    print("-" * 50)
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            print("\n🌳 Importance of Forests 🌳")
            print("1. Forests are the lungs of our planet, producing oxygen and absorbing carbon dioxide.")
            print("2. They provide habitat to millions of species and support biodiversity.")
            print("3. Forests help regulate the water cycle and prevent soil erosion.")
        
        elif choice == "2":
            print("\n🦁 Importance of Wildlife 🐾")
            print("1. Wildlife maintains ecological balance and contributes to ecosystems.")
            print("2. Many species provide essential services, such as pollination and pest control.")
            print("3. Wildlife contributes to cultural, recreational, and scientific enrichment.")
        
        elif choice == "3":
            print("\n🌲 Ways to Conserve Forests 🌲")
            print("1. Plant more trees (Afforestation).")
            print("2. Reduce deforestation by promoting sustainable logging.")
            print("3. Support policies that protect forests and encourage eco-friendly practices.")
        
        elif choice == "4":
            print("\n🐾 Ways to Conserve Wildlife 🦉")
            print("1. Protect habitats by establishing wildlife sanctuaries and national parks.")
            print("2. Avoid poaching and illegal wildlife trade.")
            print("3. Promote coexistence through awareness and community participation.")
        
        elif choice == "5":
            print("\nThank you for learning about forest and wildlife conservation! 🌎")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the awareness program
display_awareness()
