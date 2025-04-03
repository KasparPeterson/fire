import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import MonthlyReports from './components/MonthlyReports';
import { reportData } from './data/reports';

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
