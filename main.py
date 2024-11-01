import streamlit as st
import speedtest

def main():
    st.title("Network Speed Test")
    st.write("This test measures your download speed, which should match closely to fast.com.")

    # Start speed test when the button is pressed
    if st.button("Run Speed Test"):
        st.write("Running the test, please wait...")
        
        try:
            # Initialize the speedtest and get the best server
            speed_test = speedtest.Speedtest()
            speed_test.get_best_server()
            
            # Measure download speed in bits per second, then convert to Mbps
            download_speed_bps = speed_test.download()
            download_speed_mbps = download_speed_bps / 1_000_000  # Convert to Mbps
            
            # Display results
            st.success("Download Speed Test Result:")
            st.metric("Download Speed", f"{download_speed_mbps:.2f} Mbps")

        except Exception as e:
            st.error("Error occurred during speed test. Please try again.")
            st.write(e)

if __name__ == "__main__":
    main()
