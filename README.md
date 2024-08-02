# My Dash App

This is a Dash app that explores trends from the worldometer coronavirus daily data.

Kaggle: [Dataset source](https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset)

## Project File Structure

```
project-directory/
├── assets/
├── callbacks/
│   └── update_charts.py          # Contains the callback function for updating charts in the app from the data.
├── components/
│   └── navbar.py                 # Contains the navbar layout & styles.
├── data/
│   └── worldometer_coronavirus_daily_data.csv  # The data used for the app visualizations.
├── pages/
│   ├── countries_list.txt        # Helper data to render the country options for the app's drop-down country selection feature.
│   └── home.py                   # Contains the app's main page layout, styles, and features.
├── utils/
│   └── data_loader.py            # Helper code to load & preprocess the data.
├── venv/
├── .gitignore
├── app.py                        # Main entry point for the Dash application. Initializes the app, sets up the layout, and registers callbacks.
├── env_setup_run.py              # Python script to setup the environment and run the Dash app locally.
├── README.md
├── render.yaml                   # Yaml file for Render Cloud deployment.
└── requirements.txt              # Lists the Python dependencies required to run the app.
```

## Requirements

- Python 3.10 or 3.11
- `pip` (Python package installer)

## Setup & Run

1. **Clone the repository**

    ```sh
    git clone https://github.com/3awny/interactive-viz-ahmedawny.git
    cd interactive-viz-ahmedawny
    ```

2. **Execute the setup & run script**
    Use this script to setup the environment & run the app locally.
    ```sh
    python env_setup_run.py
    ```

3. **Access the app (locally)**
    
    If step 2 above is completed you can view the app here
    - **Locally**: Open your web browser and go to [http://127.0.0.1:8050](http://127.0.0.1:8050/).


## Access the app (deployed)

Production: The app is currently deployed at [https://interactive-viz-ahmedawny.onrender.com](https://interactive-viz-ahmedawny.onrender.com).

**Note:** Because a free tier web service is used, the service spins down when there is no activity for certain amount of time. If it's in a down state at the time you visit the link, you won't see the page straight away. Please wait up to 1 minute max for the service to spin-up, it will appear to you that the page is loading during that time. Rest assured, it will not take longer than 1 minute.
