import React, { useState } from "react";
import { Box, Button, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { mockTransactions } from "../../data/mockData";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import DoneIcon from '@mui/icons-material/Done';
import LockOpenIcon from '@mui/icons-material/LockOpen';
import CancelIcon from '@mui/icons-material/Cancel';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";
import GeographyChart from "../../components/GeographyChart";
import BarChart from "../../components/BarChart";
import StatBox from "../../components/StatBox";
import ProgressCircle from "../../components/ProgressCircle";
import Test from "../../components/Test";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [isOpen, setIsOpen] = useState(false);
  return (
    <Box m="10px"
    >
      {/* HEADER */}
      <Box

        display="grid"
        gridTemplateColumns={{ xs: 'repeat(1, 1fr)', sm: 'repeat(4, 1fr)', md: 'repeat(4, 1fr)' }}
        gridAutoRows={{ xs: "70px", sm: '70px', md: '70px' }}
        gridColumn={{ xs: 'span 1', sm: 'span 8', md: 'span 8' }}
        gap="20px"
      >
        <Header title="DASHBOARD" subtitle="Welcome to xira" />

        <Box
        >
          <Button
            sx={{
              backgroundColor: colors.blueAccent[700],
              color: colors.grey[100],
              fontSize: "14px",
              fontWeight: "bold",
            }}
          >
            <DownloadOutlinedIcon sx={{ mr: "10px" }} />
            Download Reports
          </Button>
        </Box>
      </Box>
      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns={{ xs: 'repeat(12, 1fr)', sm: 'repeat(12, 1fr)', md: 'repeat(12, 1fr)' }}
        gridAutoRows="140px"
        gap="20px"
      >
        {/* ROW 1 */}
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 3' }}
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="12,361"
            subtitle="Resolved Tickets"
            progress="0.75"
            increase="+14%"
            icon={
              <DoneIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 3' }}
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="431,225"
            subtitle="Open Tickets"
            progress="0.50"
            increase="+21%"
            icon={
              <LockOpenIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 3' }}
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
          onClick={() => setIsOpen(!isOpen)}
        >
          <StatBox
            title="32,441"
            subtitle="Closed Tickets"
            progress="0.30"
            increase="+5%"
            icon={
              <CancelIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 3' }}
          backgroundColor={colors.primary[400]}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="1,325,134"
            subtitle="Pending Tickets"
            progress="0.80"
            increase="+43%"
            icon={
              <MoreHorizIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>

        {/* ROW 2 */}
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 8' }}
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Box

          >
            <Box>
              <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
              >
                Queries Resolved
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
              >
                9,342
              </Typography>
            </Box>
            <Box>
              <IconButton>
                <DownloadOutlinedIcon
                  sx={{ fontSize: "26px", color: colors.greenAccent[500] }}
                />
              </IconButton>
            </Box>
          </Box>
          <Box height="250px" m="-20px 0 0 0">
            <LineChart isDashboard={true} />
          </Box>
        </Box>
        {isOpen &&
          <Test />
          // <Box
          //   gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
          //   gridRow="span 2"
          //   backgroundColor={colors.primary[400]}
          //   overflow="auto"
          // >
          //   <Box
          //     gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
          //     gridRow="span 2"
          //     backgroundColor={colors.primary[400]}
          //     padding="10px"
          //   >
          //     <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
          //       Recent Tickets
          //     </Typography>
          //   </Box>
          //   {mockTransactions.map((transaction, i) => (
          //     <Box
          //       key={`${transaction.txId}-${i}`}
          //       display="flex"
          //       justifyContent="space-between"
          //       alignItems="center"
          //       borderBottom={`4px solid ${colors.primary[500]}`}
          //       p="15px"
          //     >
          //       <Box>
          //         <Typography
          //           color={colors.greenAccent[500]}
          //           variant="h5"
          //           fontWeight="600"
          //         >
          //           {transaction.txId}
          //         </Typography>
          //         <Typography color={colors.grey[100]}>
          //           {transaction.user}
          //         </Typography>
          //       </Box>
          //       <Box color={colors.grey[100]}>{transaction.date}</Box>
          //       <Box
          //         backgroundColor={colors.greenAccent[500]}
          //         p="5px 10px"
          //         borderRadius="4px"
          //       >
          //         ${transaction.cost}
          //       </Box>
          //     </Box>
          //   ))}
          // </Box>
        }

        {/* ROW 3 */}
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          padding="10px"

        >
          <Typography variant="h5" fontWeight="600">
            Query Summary
          </Typography>
          <Box
            gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
            gridRow="span 2"
            backgroundColor={colors.primary[400]}
          >
            <ProgressCircle size="125" />
            <Typography
              variant="h5"
              color={colors.greenAccent[500]}
              sx={{ mt: "15px" }}
            >
              48 352 tickets solved
            </Typography>
            <Typography>Overall tickets</Typography>
          </Box>
        </Box>
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          padding="10px"
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ padding: "10px 10px 0 10px" }}
          >
            tickets Quantity
          </Typography>
          <Box
            height="250px"
            gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
            gridRow="span 2"
            backgroundColor={colors.primary[400]}
            padding="10px"
          >
            <BarChart isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn={{ xs: 'span 12', sm: 'span 6', md: 'span 4' }}
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          padding="10px"
        >
          <Typography
            variant="h5"
            fontWeight="600"
            sx={{ marginBottom: "15px" }}
          >
            Geography Based Tickets
          </Typography>
          <Box height="200px">
            <GeographyChart isDashboard={true} />
          </Box>
        </Box>
      </Box >
    </Box >
  );
};

export default Dashboard;
