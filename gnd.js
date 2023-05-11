const getData = async () => {
  response = await fetch("https://lobid.org/gnd/4026761-1.json");
  result = await response.json();
  console.log(response);
  console.log("Hello");
};
