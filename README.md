# the-reserves

This is an alternative open-source Zoom workspace reservation system, designed to be fully operational in an air-gapped and self-managed environment. It allows users to efficiently reserve workspaces for specific time slots, integrating seamlessly into facilities without internet connectivity.
Features

    User Management: Allows the creation and management of user accounts, with capabilities to add, edit, and deactivate users.

    Workspace Management: Administrators can define and configure workspace settings including location, capacity, and availability.

    Floorplan Management: Users can upload a floorplan of their facility and interactively select workspaces directly from the floorplan to make reservations.

    Reservation Management: Supports making, viewing, and managing reservations with options to modify or cancel existing bookings.

    Air-gapped Capability: Fully functional without any internet connection, ensuring data privacy and security.

Requirements

    Python 3.8 or newer
    SQLite3

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/zoom-workspace-reservation.git

Navigate to the project directory:

bash

cd zoom-workspace-reservation

Install necessary Python packages:

pip install -r requirements.txt

Run the application:

css

    python main.py

Usage

Here is how you can get started with making reservations:

    Create a user:

    python

user = User(name="John Doe")
user.save()

Define a workspace:

python

workspace = Workspace(location="101", capacity=4)
workspace.save()

Make a reservation:

python

    reservation = Reservation(user=user, workspace=workspace, start_time="09:00", end_time="17:00")
    reservation.save()

Contributing

We welcome contributions to this project. If you're interested in helping out, please fork the repository, make your changes, and submit a pull request. We're excited to see what you come up with!

For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate.
License

This project is licensed under the MIT License.
