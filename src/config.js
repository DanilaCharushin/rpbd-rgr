let CONFIG;

if (process.env.NODE_ENV === "development") {
  CONFIG = {
    host: "http://127.0.0.1:8000"
  };
} else {
  CONFIG = {
    host: "https://rpbd-rgr.herokuapp.com"
    // host: "http://127.0.0.1:8000"
  };
}

export default CONFIG;
