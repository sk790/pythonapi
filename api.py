from flask import Flask, request, jsonify

app = Flask(__name__)

indian_population = [
  {
    "Year": 2024,
    "Population": 1450935791,
    "Yearly % Change": "0.89 %",
    "Yearly Change": 12866195,
    "Migrants (net)": -630830,
    "Median Age": 28.4,
    "Fertility Rate": 1.96,
    "Density (P/Km²)": 488,
    "Urban Pop %": "36.6 %",
    "Urban Population": 530387142,
    "Country's Share of World Pop": "17.78 %",
    "World Population": 8161972572,
    "India Global Rank": 1
  },
  {
    "Year": 2023,
    "Population": 1438069596,
    "Yearly % Change": "0.89 %",
    "Yearly Change": 12646384,
    "Migrants (net)": -979179,
    "Median Age": 28.1,
    "Fertility Rate": 1.98,
    "Density (P/Km²)": 484,
    "Urban Pop %": "36.0 %",
    "Urban Population": 518239122,
    "Country's Share of World Pop": "17.77 %",
    "World Population": 8091734930,
    "India Global Rank": 1
  },
  {
    "Year": 2022,
    "Population": 1425423212,
    "Yearly % Change": "0.79 %",
    "Yearly Change": 11219316,
    "Migrants (net)": -1353478,
    "Median Age": 27.7,
    "Fertility Rate": 1.99,
    "Density (P/Km²)": 479,
    "Urban Pop %": "35.5 %",
    "Urban Population": 506304869,
    "Country's Share of World Pop": "17.77 %",
    "World Population": 8021407192,
    "India Global Rank": 1
  },
  {
    "Year": 2020,
    "Population": 1402617695,
    "Yearly % Change": "0.98 %",
    "Yearly Change": 13587383,
    "Migrants (net)": -73806,
    "Median Age": 27,
    "Fertility Rate": 2.05,
    "Density (P/Km²)": 472,
    "Urban Pop %": "34.4 %",
    "Urban Population": 483098640,
    "Country's Share of World Pop": "17.78 %",
    "World Population": 7887001292,
    "India Global Rank": 2
  },
  {
    "Year": 2015,
    "Population": 1328024498,
    "Yearly % Change": "1.32 %",
    "Yearly Change": 16908587,
    "Migrants (net)": -655085,
    "Median Age": 25.3,
    "Fertility Rate": 2.29,
    "Density (P/Km²)": 447,
    "Urban Pop %": "32.3 %",
    "Urban Population": 429069459,
    "Country's Share of World Pop": "17.78 %",
    "World Population": 7470491872,
    "India Global Rank": 2
  },
  {
    "Year": 2010,
    "Population": 1243481564,
    "Yearly % Change": "1.49 %",
    "Yearly Change": 17761048,
    "Migrants (net)": -50905,
    "Median Age": 23.6,
    "Fertility Rate": 2.60,
    "Density (P/Km²)": 418,
    "Urban Pop %": "30.6 %",
    "Urban Population": 380744554,
    "Country's Share of World Pop": "17.71 %",
    "World Population": 7021732148,
    "India Global Rank": 2
  },
  {
    "Year": 2005,
    "Population": 1154676322,
    "Yearly % Change": "1.77 %",
    "Yearly Change": 19350718,
    "Migrants (net)": -929454,
    "Median Age": 22.2,
    "Fertility Rate": 2.96,
    "Density (P/Km²)": 388,
    "Urban Pop %": "29.0 %",
    "Urban Population": 334479406,
    "Country's Share of World Pop": "17.53 %",
    "World Population": 6586970132,
    "India Global Rank": 2
  },
  {
    "Year": 2000,
    "Population": 1057922733,
    "Yearly % Change": "1.96 %",
    "Yearly Change": 19524338,
    "Migrants (net)": -143960,
    "Median Age": 21.2,
    "Fertility Rate": 3.35,
    "Density (P/Km²)": 356,
    "Urban Pop %": "27.5 %",
    "Urban Population": 291350282,
    "Country's Share of World Pop": "17.14 %",
    "World Population": 6171702993,
    "India Global Rank": 2
  },
  {
    "Year": 1995,
    "Population": 960301044,
    "Yearly % Change": "2.11 %",
    "Yearly Change": 19065765,
    "Migrants (net)": -57297,
    "Median Age": 20.3,
    "Fertility Rate": 3.65,
    "Density (P/Km²)": 323,
    "Urban Pop %": "26.6 %",
    "Urban Population": 255558824,
    "Country's Share of World Pop": "16.68 %",
    "World Population": 5758878982,
    "India Global Rank": 2
  },
  {
    "Year": 1990,
    "Population": 864972221,
    "Yearly % Change": "2.28 %",
    "Yearly Change": 18464886,
    "Migrants (net)": 125514,
    "Median Age": 19.7,
    "Fertility Rate": 4.05,
    "Density (P/Km²)": 291,
    "Urban Pop %": "25.7 %",
    "Urban Population": 222296728,
    "Country's Share of World Pop": "16.24 %",
    "World Population": 5327803110,
    "India Global Rank": 2
  },
  {
    "Year": 1985,
    "Population": 772647793,
    "Yearly % Change": "2.37 %",
    "Yearly Change": 17058754,
    "Migrants (net)": -89991,
    "Median Age": 19.3,
    "Fertility Rate": 4.43,
    "Density (P/Km²)": 260,
    "Urban Pop %": "24.6 %",
    "Urban Population": 190321782,
    "Country's Share of World Pop": "15.87 %",
    "World Population": 4868943465,
    "India Global Rank": 2
  },
  {
    "Year": 1980,
    "Population": 687354025,
    "Yearly % Change": "2.37 %",
    "Yearly Change": 15208898,
    "Migrants (net)": 210914,
    "Median Age": 18.9,
    "Fertility Rate": 4.78,
    "Density (P/Km²)": 231,
    "Urban Pop %": "23.4 %",
    "Urban Population": 160941941,
    "Country's Share of World Pop": "15.45 %",
    "World Population": 4447606236,
    "India Global Rank": 2
  },
  {
    "Year": 1975,
    "Population": 611309535,
    "Yearly % Change": "2.29 %",
    "Yearly Change": 13089053,
    "Migrants (net)": 434205,
    "Median Age": 18.4,
    "Fertility Rate": 5.20,
    "Density (P/Km²)": 206,
    "Urban Pop %": "21.7 %",
    "Urban Population": 132533810,
    "Country's Share of World Pop": "15.02 %",
    "World Population": 4070735277,
    "India Global Rank": 2
  },
  {
    "Year": 1970,
    "Population": 545864268,
    "Yearly % Change": "2.18 %",
    "Yearly Change": 11144824,
    "Migrants (net)": 233782,
    "Median Age": 18.1,
    "Fertility Rate": 5.62,
    "Density (P/Km²)": 184,
    "Urban Pop %": "20.0 %",
    "Urban Population": 109388950,
    "Country's Share of World Pop": "14.77 %",
    "World Population": 3694683794,
    "India Global Rank": 2
  },
  {
    "Year": 1965,
    "Population": 490140146,
    "Yearly % Change": "2.37 %",
    "Yearly Change": 10829962,
    "Migrants (net)": -248299,
    "Median Age": 18.5,
    "Fertility Rate": 5.94,
    "Density (P/Km²)": 165,
    "Urban Pop %": "19.1 %",
    "Urban Population": 93493844,
    "Country's Share of World Pop": "14.70 %",
    "World Population": 3334533703,
    "India Global Rank": 2
  },
  {
    "Year": 1960,
    "Population": 435990338,
    "Yearly % Change": "2.38 %",
    "Yearly Change": 9657890,
    "Migrants (net)": 146955,
    "Median Age": 19.2,
    "Fertility Rate": 5.92,
    "Density (P/Km²)": 147,
    "Urban Pop %": "18.5 %",
    "Urban Population": 80565723,
    "Country's Share of World Pop": "14.46 %",
    "World Population": 3015470894,
    "India Global Rank": 2
  },
  {
    "Year": 1955,
    "Population": 387700887,
    "Yearly % Change": "2.29 %",
    "Yearly Change": 8284413,
    "Migrants (net)": 70393,
    "Median Age": 19.7,
    "Fertility Rate": 5.91,
    "Density (P/Km²)": 130,
    "Urban Pop %": "18.6 %",
    "Urban Population": 71958495,
    "Country's Share of World Pop": "14.15 %",
    "World Population": 2740213792,
    "India Global Rank": 2
  }
]


@app.route('/run-+', methods=['POST'])

def run_python():
    return indian_population
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
