def payload_only(selected_engineering_option):
    return "Contact Camera Group"

def bus_only(selected_engineering_option):
    import streamlit as st
    import pandas as pd

    # pif_dat = st.file_uploader("Upload the Payload Intake Form", type= "csv")

    # file_path = '/workspaces/mapper-dashboard/data/pif_data.csv'  # Replace with the actual path to your CSV file

    # try:
    #     data = pd.read_csv(file_path)
    # except FileNotFoundError:
    #     st.error(f"File not found: {file_path}")
    #     st.stop()

    # # Ensure the CSV has the expected structure
    # if 'Parameter' not in data.columns or 'Value' not in data.columns:
    #     st.error("The CSV file must contain 'Parameter' and 'Value' columns.")
    #     st.stop()

    # # Extract payload information
    # payload_data = {
    #     "Payload Type": [],
    #     "Mass (kg)": [],
    #     "X (mm)": [],
    #     "Y (mm)": [],
    #     "Z (mm)": [],
    #     "FOV (°)": []
    # }

    # for i in range(1, 5):  # Loop through Payload 1 to Payload 4
    #     try:
    #         payload_data["Payload Type"].append(data.loc[data['Parameter'] == f'Payload {i} Type', 'Value'].values[0])
    #         payload_data["Mass (kg)"].append(int(data.loc[data['Parameter'] == f'Payload {i} Mass', 'Value'].values[0]))
    #         payload_data["X (mm)"].append(int(data.loc[data['Parameter'] == f'Payload {i} X', 'Value'].values[0]))
    #         payload_data["Y (mm)"].append(int(data.loc[data['Parameter'] == f'Payload {i} Y', 'Value'].values[0]))
    #         payload_data["Z (mm)"].append(int(data.loc[data['Parameter'] == f'Payload {i} Z', 'Value'].values[0]))
    #         payload_data["FOV (°)"].append(int(data.loc[data['Parameter'] == f'Payload {i} FOV', 'Value'].values[0]))
    #     except IndexError:
    #         st.warning(f"Data for Payload {i} is missing in the CSV file.")
    #         payload_data["Payload Type"].append("N/A")
    #         payload_data["Mass (kg)"].append(0)
    #         payload_data["X (mm)"].append(0)
    #         payload_data["Y (mm)"].append(0)
    #         payload_data["Z (mm)"].append(0)
    #         payload_data["FOV (°)"].append(0)


    # payload_df = pd.DataFrame(payload_data);


    # # Extract miscellaneous information
    # misc_parameters = [
    #     ("Mission Name", ""),
    #     ("Mission Type", ""),
    #     ("Mission Duration", "years"),
    #     ("Number of Ops Modes", ""),
    #     ("Input Voltage", "V"),
    #     ("Current", "A"),
    #     ("TMTC Interface", ""),
    #     ("Payload Database", ""),
    #     ("Mounting Points", ""),
    #     ("Fastener Type", ""),
    #     ("Data Dumping per Day", "MB"),
    #     ("Max Data Latency Hours", "hours"),
    #     ("Pointing Accuracy 3 sigma", "°"),
    #     ("Pointing Knowledge 3 sigma", "°"),
    #     ("Pointing Stability", "°/s"),
    #     ("Max Off Nadir Angle", "°"),
    #     ("Acceptable Temperature Min", "°C"),
    #     ("Acceptable Temperature Max", "°C"),
    #     ("Orbit Altitude", "km"),
    #     ("Orbit Inclination", "°"),
    #     ("LTAN (if SSO)", "hh:mm")
    # ]

    # # Generate list content
    # misc_list = []
    # for param, unit in misc_parameters:
    #     try:
    #         value = data.loc[data['Parameter'] == param, 'Value'].values[0]
    #         misc_list.append(f"**{param}:** {value} {unit}".strip())
    #     except IndexError:
    #         misc_list.append(f"**{param}:** N/A")

    # # Split the list into two equal parts
    # split_index = len(misc_list) // 2
    # column1, column2 = misc_list[:split_index+1], misc_list[split_index+1:]

    # # Display tables and lists in Streamlit
    # st.title("Payload and Mission Information")

    # st.subheader("Payload Information")
    # st.markdown(
    #     """
    #     This section presents the key payload and mission parameters and constraints derived obtained from the customer and payload intake form.
    #     """
    # )
    # def set_column_widths(df):
    #     return df.style.set_properties(
    #         **{
    #             "max-width": "150px",  # Adjust width
    #             "overflow": "hidden",
    #             "text-overflow": "ellipsis",
    #             "white-space": "nowrap"
    #         }
    #     )
    # st.dataframe(set_column_widths(payload_df), use_container_width=True)
    # st.subheader("Mission and Miscellaneous Information")
    # col1, col2 = st.columns(2)

    # with col1:
    #     st.write("\n".join([f"- {item}" for item in column1]))

    # with col2:
    #     st.write("\n".join([f"- {item}" for item in column2]))

    # # Mission Design and Analysis Output
    # st.subheader("Mission Design and Analysis Output")
    # st.markdown(
    #     """
    #     This section presents the outputs of the Mission Design and Analysis simulations conducted on STK. 
    #     These results are derived based on the payload requirements, orbit parameters, 
    #     and system constraints provided in the intake form.
    #     """
    # )
    # mda_path = '/workspaces/mapper-dashboard/data/mda_data.csv'
    # chemical_thrust_path = '/workspaces/mapper-dashboard/data/chemical_thrust_data.csv'
    # electric_thrust_path = '/workspaces/mapper-dashboard/data/electric_thrust_data.csv'
    # initial_sun_panel_angle_path = '/workspaces/mapper-dashboard/data/initial_sun_panel_angle_data.csv'
    # final_sun_panel_angle_path = '/workspaces/mapper-dashboard/data/final_sun_panel_angle_data.csv'

    # # Load CSV data into DataFrames
    # try:
    #     mda_df = pd.read_csv(mda_path)
    #     chemical_thrust_df = pd.read_csv(chemical_thrust_path)
    #     electric_thrust_df = pd.read_csv(electric_thrust_path)
    #     initial_sun_panel_angle_df = pd.read_csv(initial_sun_panel_angle_path)
    #     final_sun_panel_angle_df = pd.read_csv(final_sun_panel_angle_path)
    # except Exception as e:
    #     st.error(f"Error loading data: {e}")
    #     st.stop()

    # st.subheader("Mission Data")
    # st.dataframe(set_column_widths(mda_df), use_container_width=True)

    # st.subheader("Chemical Thrust Data")
    # st.dataframe(set_column_widths(chemical_thrust_df), use_container_width=True)

    # st.subheader("Electric Thrust Data")
    # st.dataframe(set_column_widths(electric_thrust_df), use_container_width=True)

    # st.subheader("Initial Sun Panel Angle Data")
    # st.dataframe(set_column_widths(initial_sun_panel_angle_df), use_container_width=True)

    # st.subheader("Final Sun Panel Angle Data")
    # st.dataframe(set_column_widths(final_sun_panel_angle_df), use_container_width=True)


    # # Define the options for the dropdown
    # sat_class_options = [50, 100, 200, 500]

    # # Create the dropdown
    # sat_class_selected_option = st.selectbox("Select your satellite class (kg):", sat_class_options)

    # # Display the selected option
    # if sat_class_selected_option < payload_df.iloc[0][1]+payload_df.iloc[1][1]+payload_df.iloc[2][1]+payload_df.iloc[3][1]:
    #     st.write("Bus class cannot be less than payload weight!!")
    return "OK"