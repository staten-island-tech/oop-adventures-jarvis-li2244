class GUI():
    def actions():
        ere =int(input(""))
        GUI.atk_gui() if ere == 1 else(GUI.run_gui() if ere == 2 else(GUI.equip_gui() if ere == 3 else(GUI.items_gui() if ere == 4 else GUI.actions())))
    def run_gui():
        print(r""" 

            ╔═════════════════════════╗
            ║     ESCAPE SUCESSFUL    ║
            ╚═════════════════════════╝
                """)
        print(r""" 
            ╔═════════════════════════╗
            ║      ESCAPE FAILED      ║
            ╚═════════════════════════╝
                """)
        
    def atk_gui():
        var1 = 4564456
        print(f"""
    ╔═════════════════════════╗
    ║    {var1} DMG Dealt     ║
    ╚═════════════════════════╝
            """)
    def equip_gui():
        print(r"""
            """)
    def items_gui():
        item_name = "EGG"
        print(f'''
    ══════════════════════════════════
    1. {item_name}                             
    ══════════════════════════════════
    2. {item_name}                             
    ══════════════════════════════════
    3. {item_name}                             
    ══════════════════════════════════
    4. {item_name}                             
    ══════════════════════════════════
    5. {item_name}                             
    ══════════════════════════════════
    6. {item_name}                             
    ══════════════════════════════════
    7. {item_name}                             
    ══════════════════════════════════
    8. {item_name}                             
    ══════════════════════════════════
    9. {item_name}                             
    ══════════════════════════════════
                ''')
    y = 34
    def item_desc():
        print(r"""







                """)

    #settings for health and mana bars to simplify them 102102010 to 100
    def settings_GUI():
        print(r"""





            """)