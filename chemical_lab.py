import streamlit as st

# Custom HTML code for the head section
custom_head_html = """
<head>
    <!-- Your custom HTML code goes here -->
    <title>Chemical Lab</title>
    <meta name="description" content="chemical lab for experiments">
    <!-- Add more custom meta tags, stylesheets, scripts, etc. -->
            <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RT67Y28Q1H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-RT67Y28Q1H');
</script>
</head>
"""

# Streamlit app title
st.markdown(custom_head_html, unsafe_allow_html=True)
# Elements list
elements = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'H20','O2','Ne','HCl',
    'HNO','HSO4','Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca'
]

# Reactions dictionary (you can add more reactions)
reactions = {
    ('H', 'O'): {
        'products': 'H2O',
        'reaction': '2H2 + O2 -> 2H2O',
        'type': 'Combustion',
        'energy_change': -286,  # kJ/mol
        'uses': 'Water production'
    },
    ('H', 'H'):  {
    'products': 'H2',
    'reaction': '2H -> H2',
    'type': 'Synthesis',
    'energy_change': -436.0,  # kJ/mol (dissociation energy of H2)
    'uses': 'Formation of hydrogen gas'
    },

    ('Na', 'CL'): {
        'products': 'NaCl',
        'reaction': '2Na + Cl2 -> 2NaCl',
        'type': 'Synthesis',
        'energy_change': -411,  # kJ/mol
        'uses': 'Salt production'
    },
    ('C', 'O'): {
        'products': 'CO2',
        'reaction': 'C + O2 -> CO2',
        'type': 'Combustion',
        'energy_change': -393.5,  # kJ/mol
        'uses': 'Carbon dioxide production'
    },
    ('H', 'Cl'): {
        'products': 'HCl',
        'reaction': 'H2 + Cl2 -> 2HCl',
        'type': 'Synthesis',
        'energy_change': -92.3,  # kJ/mol
        'uses': 'Hydrochloric acid production'
    },
    ('H', 'N'): {
        'products': 'NH3',
        'reaction': 'N2 + 3H2 -> 2NH3',
        'type': 'Synthesis',
        'energy_change': -46.2,  # kJ/mol
        'uses': 'Ammonia production'
    },
    ('C', 'Cl'): {
        'products': 'CCl4',
        'reaction': 'C + 2Cl2 -> CCl4',
        'type': 'Synthesis',
        'energy_change': -95.7,  # kJ/mol
        'uses': 'Carbon tetrachloride production'
    },
    ('O', 'F'): {
        'products': 'OF2',
        'reaction': 'O2 + 2F2 -> 2OF2',
        'type': 'Synthesis',
        'energy_change': -118.2,  # kJ/mol
        'uses': 'Oxygen difluoride production'
    },
    ('MG', 'O'): {
        'products': 'MgO',
        'reaction': '2Mg + O2 -> 2MgO',
        'type': 'Synthesis',
        'energy_change': -601.6,  # kJ/mol
        'uses': 'Magnesium oxide production'
    },
    ('C', 'H'): {
        'products': 'CH4',
        'reaction': 'C + 2H2 -> CH4',
        'type': 'Synthesis',
        'energy_change': -74.9,  # kJ/mol
        'uses': 'Methane production'
    },
    ('C', 'N'): {
        'products': 'HCN',
        'reaction': 'C + N2 -> HCN',
        'type': 'Synthesis',
        'energy_change': +132.9,  # kJ/mol
        'uses': 'Hydrogen cyanide production'
    },
    ('S', 'O'): {
        'products': 'SO2',
        'reaction': 'S + O2 -> SO2',
        'type': 'Combustion',
        'energy_change': -296.8,  # kJ/mol
        'uses': 'Sulfur dioxide production'
    },
    ('P', 'O'): {
        'products': 'P4O10',
        'reaction': 'P4 + 5O2 -> P4O10',
        'type': 'Combustion',
        'energy_change': -2967,  # kJ/mol
        'uses': 'Phosphorus pentoxide production'
    },
    ('C', 'S'): {
        'products': 'CS2',
        'reaction': 'C + 2S -> CS2',
        'type': 'Synthesis',
        'energy_change': +89.4,  # kJ/mol
        'uses': 'Carbon disulfide production'
    },
    ('H', 'S'): {
        'products': 'H2S',
        'reaction': 'H2 + S -> H2S',
        'type': 'Synthesis',
        'energy_change': -20.1,  # kJ/mol
        'uses': 'Hydrogen sulfide production'
    },
    ('O', 'Cl'): {
        'products': 'Cl2O7',
        'reaction': '2Cl2 + 7O2 -> 2Cl2O7',
        'type': 'Synthesis',
        'energy_change': -93.5,  # kJ/mol
        'uses': 'Chlorine heptoxide production'
    },
    ('Mg', 'H'): {
        'products': 'MgH2',
        'reaction': 'Mg + H2 -> MgH2',
        'type': 'Synthesis',
        'energy_change': -73.1,  # kJ/mol
        'uses': 'Magnesium hydride production'
    },
    ('Mg', 'CL'): {
        'products': 'MgCl2',
        'reaction': 'Mg + Cl2 -> MgCl2',
        'type': 'Synthesis',
        'energy_change': -641.2,  # kJ/mol
        'uses': 'Magnesium chloride production'
    },
    ('AL', 'O'): {
        'products': 'Al2O3',
        'reaction': '4Al + 3O2 -> 2Al2O3',
        'type': 'Synthesis',
        'energy_change': -1676.6,  # kJ/mol
        'uses': 'Aluminum oxide production'
    },
    ('C', 'F'): {
        'products': 'CF4',
        'reaction': 'C + 2F2 -> CF4',
        'type': 'Synthesis',
        'energy_change': -679,  # kJ/mol
        'uses': 'Carbon tetrafluoride production'
    },
    ('H', 'F'): {
        'products': 'HF',
        'reaction': 'H2 + F2 -> 2HF',
        'type': 'Synthesis',
        'energy_change': -273,  # kJ/mol
        'uses': 'Hydrofluoric acid production'
    },
    ('N', 'O'): {
        'products': 'NO',
        'reaction': 'N2 + O2 -> 2NO',
        'type': 'Synthesis',
        'energy_change': +90.3,  # kJ/mol
        'uses': 'Nitric oxide production'
    },
   ('Mg', 'F'): {
        'products': 'MgF2',
        'reaction': 'Mg + F2 -> MgF2',
        'type': 'Synthesis',
        'energy_change': -1120  # kJ/mol
    },

    ('H', 'O'): {
        'products': 'H2O',
        'reaction': '2H2 + O2 -> 2H2O',
        'type': 'Combustion',
        'energy_change': -286,  # kJ/mol
        'uses': 'Water production'
    },
    ('Na', 'CL'): {
        'products': 'NaCl',
        'reaction': '2Na + Cl2 -> 2NaCl',
        'type': 'Synthesis',
        'energy_change': -411,  # kJ/mol
        'uses': 'Salt production'
    },
    ('Li', 'H2O'): {
            'products': 'LiOH + H2',
            'reaction': '2Li + 2H2O -> 2LiOH + H2',
            'type': 'Single Replacement',
            'energy_change': -95.3,  # kJ/mol
            'uses': 'Production of lithium hydroxide and hydrogen gas'
        },
        ('Li', 'N2'): {
            'products': 'Li3N',
            'reaction': '6Li + N2 -> 2Li3N',
            'type': 'Synthesis',
            'energy_change': +77.2,  # kJ/mol
            'uses': 'Production of lithium nitride'
        },
        ('Li', 'O2'): {
            'products': 'Li2O',
            'reaction': '4Li + O2 -> 2Li2O',
            'type': 'Synthesis',
            'energy_change': -597.6,  # kJ/mol
            'uses': 'Production of lithium oxide'
        },
        ('Li', 'HCL'): {
            'products': 'LiCl + H2',
            'reaction': 'Li + HCl -> LiCl + H2',
            'type': 'Single Replacement',
            'energy_change': -58.8,  # kJ/mol
            'uses': 'Production of lithium chloride and hydrogen gas'
        },
        ('Li', 'S'): {
            'products': 'Li2S',
            'reaction': '8Li + S8 -> 4Li2S',
            'type': 'Synthesis',
            'energy_change': -421.6,  # kJ/mol
            'uses': 'Production of lithium sulfide'
        },
        ('Na', 'H2O'): {
            'products': 'NaOH + H2',
            'reaction': '2Na + 2H2O -> 2NaOH + H2',
            'type': 'Single Replacement',
            'energy_change': -83.6,  # kJ/mol
            'uses': 'Production of sodium hydroxide and hydrogen gas'
        },
        ('Na', 'N2'): {
            'products': 'NaN3',
            'reaction': '6Na + N2 -> 2NaN3',
            'type': 'Synthesis',
            'energy_change': +101.7,  # kJ/mol
            'uses': 'Production of sodium azide'
        },
        ('Na', 'O2'): {
            'products': 'Na2O2',
            'reaction': '2Na + O2 -> Na2O2',
            'type': 'Synthesis',
            'energy_change': -378,  # kJ/mol
            'uses': 'Production of sodium peroxide'
        },
        ('Na', 'HCl'): {
            'products': 'NaCl + H2',
            'reaction': 'Na + HCl -> NaCl + H2',
            'type': 'Single Replacement',
            'energy_change': -57.1,  # kJ/mol
            'uses': 'Production of sodium chloride and hydrogen gas'
        },
        ('Na', 'S'): {
            'products': 'Na2S',
            'reaction': '2Na + S8 -> Na2S',
            'type': 'Synthesis',
            'energy_change': -371.6,  # kJ/mol
            'uses': 'Production of sodium sulfide'
        },
        ('K', 'H2O'): {
            'products': 'KOH + H2',
            'reaction': '2K + 2H2O -> 2KOH + H2',
            'type': 'Single Replacement',
            'energy_change': -57.6,  # kJ/mol
            'uses': 'Production of potassium hydroxide and hydrogen gas'
        },
        ('K', 'N2'): {
            'products': 'KN3',
            'reaction': '6K + N2 -> 2KN3',
            'type': 'Synthesis',
            'energy_change': +83.7,  # kJ/mol
            'uses': 'Production of potassium azide'
        },
        ('K', 'O2'): {
            'products': 'K2O',
            'reaction': '4K + O2 -> 2K2O',
            'type': 'Synthesis',
            'energy_change': -419.2,  # kJ/mol
            'uses': 'Production of potassium oxide'
        },
        ('K', 'HCL'): {
            'products': 'KCl + H2',
            'reaction': 'K + HCl -> KCl + H2',
            'type': 'Single Replacement',
            'energy_change': -36.4,  # kJ/mol
            'uses': 'Production of potassium chloride and hydrogen gas'
        },
        ('K', 'S'): {
            'products': 'K2S',
            'reaction': '8K + S8 -> 4K2S',
            'type': 'Synthesis',
            'energy_change': -414.4,  # kJ/mol
            'uses': 'Production of potassium sulfide'
        },
    # Add more reactions here...
}

def display_reaction_info(reactants, reaction_info):
    st.subheader("Reaction Information:")
    st.write(f"Reactants: {reactants[0]} and {reactants[1]}")
    st.write(f"Products: {reaction_info['products']}")
    st.write(f"Reaction: {reaction_info['reaction']}")
    st.write(f"Type: {reaction_info['type']}")
    st.write(f"Energy Change: {reaction_info['energy_change']} kJ/mol")
    st.write(f"Uses: {reaction_info['uses']}")


def main():
    st.title("Chemical Lab")

    # User input
    # first_element = st.selectbox("Select the first element:", elements)
    # second_element = st.selectbox("Select the second element:", elements)
    first_element = st.selectbox("Select the first element:", [element.capitalize() for element in elements])
    second_element = st.selectbox("Select the second element:", [element.capitalize() for element in elements])

    # Convert user inputs to lowercase
    # first_element = first_element.capitalize()
    # second_element = second_element.capitalize()

    # Display reaction info if exists
    reaction_info = reactions.get(tuple(sorted([first_element, second_element])))

    if reaction_info:
        display_reaction_info((first_element, second_element), reaction_info)
    else:
        st.error("No known reaction for these elements.")

if __name__ == "__main__":
    main()
# def main():
#     st.title("Chemical Simulator")

#     # User input
#     first_element = st.selectbox("Select the first element:", [element.capitalize() for element in elements])
#     second_element = st.selectbox("Select the second element:", [element.capitalize() for element in elements])

# # def main():
#     st.sidebar.title("Welcome to the Chemical Lab")
#     st.sidebar.write("Enter two elements below to see the reaction.")

#     # User input
#     first_element = st.sidebar.selectbox("Select the first element:", [element.capitalize() for element in elements])
#     second_element = st.sidebar.selectbox("Select the second element:", [element.capitalize() for element in elements])

#     # Display reaction info if exists
#     reaction_info = reactions.get(tuple(sorted([first_element, second_element])))
#     if reaction_info:
#         display_reaction_info((first_element, second_element), reaction_info)
#     else:
#         st.error("No known reaction for these elements.")

# if __name__ == "__main__":
#     main()

# def main():
#     # Get screen size
#     is_mobile = st.query_params.get('is_mobile', False)

#     if is_mobile:
#         st.title("Chemical Lab")
#         st.sidebar.title("Welcome to the Chemical Lab")
#         st.sidebar.write("Enter two elements below to see the reaction.")

#         # User input
#         first_element = st.selectbox("Select the first element:", elements)
#         second_element = st.selectbox("Select the second element:", elements)
#     else:
#         st.title("Chemical Lab")
#         st.write("Enter two elements below to see the reaction.")

#         # User input
#         first_element = st.sidebar.selectbox("Select the first element:", elements)
#         second_element = st.sidebar.selectbox("Select the second element:", elements)

#     # Convert user inputs to lowercase
#     first_element = first_element.capitalize()
#     second_element = second_element.capitalize()
#     #  first_element = st.selectbox("Select the first element:", [element.capitalize() for element in elements])
# #     second_element = st.selectbox("Select the second element:", [element.capitalize() for element in elements])


#     # Display reaction info if exists
#     reaction_info = reactions.get(tuple(sorted([first_element, second_element])))

#     if reaction_info:
#         display_reaction_info((first_element, second_element), reaction_info)
#     else:
#         st.error("No known reaction for these elements.")

# if __name__ == "__main__":
#     main()
