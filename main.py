import streamlit as st
import speedtest

def main():
    st.title("Network Speed Test")
    st.write("Click the button below to test your internet speed.")

    if st.button("Run Speed Test"):
        # Initialize speedtest
        st.write("Testing, please wait...")
        st.spinner("Running speed test...")
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()

        # Measure download and upload speeds
        download_speed = speed_test.download() / 1_000_000  # Mbps
        upload_speed = speed_test.upload() / 1_000_000      # Mbps
        ping = speed_test.results.ping

        # Display the results
        st.success("Speed Test Results:")
        st.metric("Download Speed", f"{download_speed:.2f} Mbps")
        st.metric("Upload Speed", f"{upload_speed:.2f} Mbps")
        st.metric("Ping", f"{ping:.0f} ms")

if __name__ == "__main__":
    main()
