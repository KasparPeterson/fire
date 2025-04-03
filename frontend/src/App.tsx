import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import SpendingChart from './components/SpendingChart';

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

const exampleData = {
  'Category.CAR': '-1240.75',
  'Category.SUPPORT_OTHERS': '-1110.00',
  'Category.RENT': '-750.00',
  'Category.GROCERIES': '-595.87',
  'Category.INVESTMENT': '-482.04',
  'Category.UTILITIES': '-402.41',
  'Category.RESTAURANT': '-263.46',
  'Category.HEALTH': '-220.84',
  'Category.KIDS': '-214.75',
  'Category.CASH_OUT': '-200.00',
  'Category.ELECTRONICS': '-90.96',
  'Category.TAXI': '-21.59',
  'Category.EDUCATION': '-20.57',
  'Category.ALCOHOL': '-19.96',
  'Category.BANK_FEES': '-13.59',
  'Category.ENTERTAINMENT': '-6.99',
  'Category.SELF': '0.00',
  'Category.INCOME': '5000.00',
};

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container>
        <SpendingChart data={exampleData} />
      </Container>
    </ThemeProvider>
  );
}

export default App;
