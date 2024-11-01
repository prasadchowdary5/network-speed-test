import streamlit as st
import speedtest

def main():
    st.title("Download Speed Test")
    st.write("Click the button below to test your internet download speed, similar to fast.com.")

    if st.button("Run Download Speed Test"):
        # Initialize speedtest
        st.write("Testing download speed, please wait...")
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()
        
        # Measure download speed only, similar to fast.com
        download_speed = speed_test.download() / 1_000_000  # Mbps
        
        # Display the result
        st.success("Download Speed Test Result:")
        st.metric("Download Speed", f"{download_speed:.2f} Mbps")

if __name__ == "__main__":
    main()
