allow pasting


const trade = async () => {
  document.getElementsByClassName("_bg-901062054")[3].click();
  await new Promise((resolve) => setTimeout(resolve, 300));
  document.getElementsByClassName("bg-greenPrimaryButtonBackground")[0].click();
  await new Promise((resolve) => setTimeout(resolve, 300));
  document.getElementsByClassName("border-b-baseBorderMed")[0].click();
  await new Promise((resolve) => setTimeout(resolve, 300));
  document.getElementsByClassName("_bg-901062054")[3].click();
  await new Promise((resolve) => setTimeout(resolve, 300));
  document.getElementsByClassName("bg-redPrimaryButtonBackground")[0].click();
  await new Promise((resolve) => setTimeout(resolve, 300));
  document.getElementsByClassName("border-b-baseBorderMed")[0].click();
};

setInterval(trade, 2800);