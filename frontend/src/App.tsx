import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import MonthlyReports from './components/MonthlyReports';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

const reportData = {
  reports: [
    {
      month: "2024-01-02",
      spendings: {
        "Category.CAR": "-1394.66",
        "Category.RESTAURANT": "-1140.66",
        "Category.SHOPPING": "-771.85",
        "Category.RENT": "-750.00",
        "Category.GROCERIES": "-563.11",
        "Category.UTILITIES": "-509.60",
        "Category.INVESTMENT": "-498.45",
        "Category.HOME": "-343.75",
        "Category.TRAVEL": "-191.09",
        "Category.HEALTH": "-152.04",
        "Category.TAXI": "-145.51",
        "Category.CASH_OUT": "-104.50",
        "Category.BANK_FEES": "-61.31",
        "Category.BEAUTY": "-48.00",
        "Category.ALCOHOL": "-21.04",
        "Category.ELECTRONICS": "-20.97",
        "Category.ENTERTAINMENT": "-12.42",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-02-01",
      spendings: {
        "Category.CAR": "-1290.77",
        "Category.GROCERIES": "-741.68",
        "Category.UTILITIES": "-648.47",
        "Category.INVESTMENT": "-497.64",
        "Category.RESTAURANT": "-485.39",
        "Category.CASH_OUT": "-404.50",
        "Category.TRAVEL": "-139.23",
        "Category.HEALTH": "-97.78",
        "Category.TAXI": "-89.81",
        "Category.ENTERTAINMENT": "-71.00",
        "Category.HOME": "-70.00",
        "Category.ALCOHOL": "-29.94",
        "Category.SUPPORT_OTHERS": "-29.00",
        "Category.ELECTRONICS": "-19.98",
        "Category.BANK_FEES": "-10.99",
        "Category.SELF": "2013.70",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-03-01",
      spendings: {
        "Category.RENT": "-1500.00",
        "Category.CAR": "-1382.53",
        "Category.GROCERIES": "-634.71",
        "Category.INVESTMENT": "-497.80",
        "Category.UTILITIES": "-375.57",
        "Category.RESTAURANT": "-345.45",
        "Category.HEALTH": "-278.32",
        "Category.TAXI": "-25.00",
        "Category.ELECTRONICS": "-20.97",
        "Category.EDUCATION": "-20.53",
        "Category.ALCOHOL": "-15.97",
        "Category.BANK_FEES": "-12.43",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-04-01",
      spendings: {
        "Category.CAR": "-1398.56",
        "Category.RESTAURANT": "-1061.22",
        "Category.RENT": "-750.00",
        "Category.TRAVEL": "-536.32",
        "Category.GROCERIES": "-526.21",
        "Category.INVESTMENT": "-497.31",
        "Category.UTILITIES": "-497.21",
        "Category.SHOPPING": "-96.64",
        "Category.HEALTH": "-49.62",
        "Category.ENTERTAINMENT": "-45.00",
        "Category.KIDS": "-44.99",
        "Category.EDUCATION": "-36.92",
        "Category.TAXI": "-24.50",
        "Category.ELECTRONICS": "-20.97",
        "Category.BANK_FEES": "-11.01",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-05-01",
      spendings: {
        "Category.UNCATEGORIZED": "-2723.64",
        "Category.CAR": "-1688.64",
        "Category.RENT": "-750.00",
        "Category.INVESTMENT": "-497.37",
        "Category.GROCERIES": "-496.40",
        "Category.RESTAURANT": "-381.54",
        "Category.UTILITIES": "-372.82",
        "Category.CASH_OUT": "-200.00",
        "Category.HEALTH": "-34.56",
        "Category.ELECTRONICS": "-21.96",
        "Category.EDUCATION": "-20.56",
        "Category.BANK_FEES": "-10.53",
        "Category.ALCOHOL": "-10.09",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.SELF": "1900.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-06-01",
      spendings: {
        "Category.UNCATEGORIZED": "-4926.90",
        "Category.CAR": "-1245.45",
        "Category.INVESTMENT": "-497.49",
        "Category.RESTAURANT": "-289.01",
        "Category.UTILITIES": "-246.43",
        "Category.TAXI": "-168.71",
        "Category.GROCERIES": "-133.94",
        "Category.ELECTRONICS": "-31.96",
        "Category.ALCOHOL": "-23.70",
        "Category.EDUCATION": "-20.84",
        "Category.BANK_FEES": "-10.50",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.HEALTH": "-4.39",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-07-01",
      spendings: {
        "Category.RENT": "-1657.56",
        "Category.CAR": "-1313.01",
        "Category.GROCERIES": "-507.05",
        "Category.INVESTMENT": "-498.08",
        "Category.TAXI": "-314.63",
        "Category.RESTAURANT": "-304.35",
        "Category.CASH_OUT": "-207.00",
        "Category.UTILITIES": "-46.75",
        "Category.EDUCATION": "-20.50",
        "Category.BANK_FEES": "-10.38",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.ELECTRONICS": "-4.97",
        "Category.SELF": "0.00",
        "Category.UNCATEGORIZED": "1743.34",
        "Category.INCOME": "5400.00"
      }
    },
    {
      month: "2024-08-01",
      spendings: {
        "Category.CAR": "-1351.94",
        "Category.RENT": "-750.00",
        "Category.INVESTMENT": "-498.19",
        "Category.GROCERIES": "-479.77",
        "Category.RESTAURANT": "-401.12",
        "Category.SUPPORT_OTHERS": "-300.00",
        "Category.CASH_OUT": "-300.00",
        "Category.KIDS": "-199.00",
        "Category.UTILITIES": "-116.75",
        "Category.HEALTH": "-95.70",
        "Category.SHOPPING": "-58.62",
        "Category.EDUCATION": "-19.93",
        "Category.TAXI": "-13.79",
        "Category.BANK_FEES": "-11.91",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.ELECTRONICS": "-3.98",
        "Category.SELF": "0.00",
        "Category.INCOME": "5150.00",
        "Category.UNCATEGORIZED": "18814.15"
      }
    },
    {
      month: "2024-09-01",
      spendings: {
        "Category.SUPPORT_OTHERS": "-1300.00",
        "Category.CAR": "-1245.44",
        "Category.RENT": "-750.00",
        "Category.GROCERIES": "-692.90",
        "Category.INVESTMENT": "-496.47",
        "Category.UNCATEGORIZED": "-470.38",
        "Category.UTILITIES": "-265.98",
        "Category.RESTAURANT": "-247.76",
        "Category.HEALTH": "-105.62",
        "Category.SHOPPING": "-44.91",
        "Category.EDUCATION": "-19.98",
        "Category.ALCOHOL": "-19.96",
        "Category.BANK_FEES": "-11.64",
        "Category.TAXI": "-6.99",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.ELECTRONICS": "-2.99",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    },
    {
      month: "2024-10-01",
      spendings: {
        "Category.CAR": "-1240.75",
        "Category.SUPPORT_OTHERS": "-1110.00",
        "Category.RENT": "-750.00",
        "Category.GROCERIES": "-595.87",
        "Category.INVESTMENT": "-482.04",
        "Category.UTILITIES": "-402.41",
        "Category.RESTAURANT": "-263.46",
        "Category.HEALTH": "-220.84",
        "Category.KIDS": "-214.75",
        "Category.CASH_OUT": "-200.00",
        "Category.ELECTRONICS": "-90.96",
        "Category.TAXI": "-21.59",
        "Category.EDUCATION": "-20.57",
        "Category.ALCOHOL": "-19.96",
        "Category.BANK_FEES": "-13.59",
        "Category.ENTERTAINMENT": "-6.99",
        "Category.SELF": "0.00",
        "Category.INCOME": "5000.00"
      }
    }
  ]
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="xl">
        <MonthlyReports reports={reportData.reports} />
      </Container>
    </ThemeProvider>
  );
}

export default App;
