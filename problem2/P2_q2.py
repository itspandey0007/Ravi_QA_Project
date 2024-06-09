
import requests

def check_application_status(url):
    """
    Check the status of the application by sending an HTTP request to the specified URL.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Application is up and running.")
        else:
            print(f"Application is down. HTTP status code: {response.status_code}")
    except requests.ConnectionError:
        print("Failed to connect to the application. It may be down or unreachable.")

def main():
    """
    Main function to run the application status checker.
    """
    # URL of the application to check
    application_url = "https://www.appdynamics.com/info/what-is-application-health-check"

    check_application_status(application_url)

if __name__ == "__main__":
    main()
