module.exports = {
  important: true,
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          100: "#2176FF",
          80: "#4D91FF",
        },
        secondary: {
          100: "#33A1FD",
          80: "#3BA3DD",
        },
        black: {
          100: "#1A2223",
          75: "#54595A",
          50: "#989C9D",
          25: "#CBCDCE",
          10: "#EAEBEB",
          5: "#F5F5F5",
        },
        white: "#FFFFFF",
        grey: "#F6F6F7",
        error: "#D7263D",
        success: "#9BC53D",
      },
      fontFamily: {
        sans: ['"Josefin Sans"', "Roboto"],
      },
      fontSize: {
        // 'p': ['14px', {
        //   lineHeight: '17px',
        //   fontWeight: '400'
        // }],
      },
    },
  },
  plugins: [],
};
