import { Box } from '@mui/material';
import SpendingChart from './SpendingChart';

interface SpendingData {
  [key: string]: string;
}

interface MonthlyReport {
  month: string;
  spendings: SpendingData;
}

interface MonthlyReportsProps {
  reports: MonthlyReport[];
}

const MonthlyReports = ({ reports }: MonthlyReportsProps) => {
  return (
    <Box sx={{ 
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(400px, 1fr))',
      gap: 3,
      p: 3
    }}>
      {reports.map((report) => (
        <Box key={report.month}>
          <SpendingChart data={report.spendings} month={report.month} />
        </Box>
      ))}
    </Box>
  );
};

export default MonthlyReports; 