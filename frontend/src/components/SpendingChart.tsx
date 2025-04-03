import { Box, Paper, Typography } from '@mui/material';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

interface SpendingData {
  [key: string]: string;
}

interface MonthlyReport {
  month: string;
  spendings: SpendingData;
}

interface SpendingChartProps {
  data: SpendingData;
  month?: string;
}

const SpendingChart = ({ data, month }: SpendingChartProps) => {
  // Filter out income and zero values, and sort by absolute value
  const filteredData = Object.entries(data)
    .filter(([_, value]) => parseFloat(value) < 0)
    .sort((a, b) => Math.abs(parseFloat(a[1])) - Math.abs(parseFloat(b[1])));

  const chartData = {
    labels: filteredData.map(([key]) => key.replace('Category.', '')),
    datasets: [
      {
        data: filteredData.map(([_, value]) => Math.abs(parseFloat(value))),
        backgroundColor: [
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0',
          '#9966FF',
          '#FF9F40',
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0',
          '#9966FF',
          '#FF9F40',
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0',
        ],
        borderWidth: 1,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'right' as const,
      },
      title: {
        display: true,
        text: month ? `Spending Analysis - ${new Date(month).toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}` : 'Monthly Spending Analysis',
        font: {
          size: 16,
        },
      },
    },
  };

  return (
    <Paper elevation={3} sx={{ p: 3, maxWidth: 800, mx: 'auto', mt: 4 }}>
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Typography variant="h4" gutterBottom>
          {month ? new Date(month).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : 'Monthly Spending Analysis'}
        </Typography>
        <Box sx={{ width: '100%', height: 400 }}>
          <Pie data={chartData} options={options} />
        </Box>
      </Box>
    </Paper>
  );
};

export default SpendingChart; 