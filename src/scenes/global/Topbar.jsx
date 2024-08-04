import { Box, IconButton, useTheme } from "@mui/material";
import { useContext, useEffect, useState } from "react";
import { ColorModeContext, tokens } from "../../theme";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import SearchIcon from "@mui/icons-material/Search";
import Sidebar from "./Sidebar";

const Topbar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext);
  const [isCollapsed, setIsCollapsed] = useState(true);
  const [selected, setSelected] = useState("Dashboard");

  useEffect(() => {
    // Get the person icon and the sidebar elements
    const personIcon = document.querySelector(".person-icon");
    const sideNav = document.querySelector(".sidebar");

    // Add a click event listener to the person icon
    if (personIcon && sideNav) {
      personIcon.addEventListener("click", () => {
        // Toggle the display of the sidebar
        sideNav.style.display = sideNav.style.display === "none" ? "block" : "none";
        setIsCollapsed((prevState) => !prevState);
      });
    }

    // Clean up the event listener when the component unmounts
    return () => {
      if (personIcon && sideNav) {
        personIcon.removeEventListener("click", () => {
          sideNav.style.display = sideNav.style.display === "none" ? "block" : "none";
          setIsCollapsed((prevState) => !prevState);
        });
      }
    };
  }, []);

  return (
    <Box display="flex" justifyContent="space-between" p={1} className="dashboard">
      {/* SEARCH BAR */}
      <Box display="flex" backgroundColor={colors.primary[400]} borderRadius="3px">
        <InputBase sx={{ ml: 2, flex: 1 }} placeholder="Search" />
        <IconButton type="button" sx={{ p: 1 }}>
          <SearchIcon />
        </IconButton>
      </Box>

      {/* ICONS */}
      <Box display="flex">
        <IconButton onClick={colorMode.toggleColorMode}>
          {theme.palette.mode === "dark" ? <DarkModeOutlinedIcon /> : <LightModeOutlinedIcon />}
        </IconButton>
        <IconButton>
          <NotificationsOutlinedIcon />
        </IconButton>
        <IconButton>
          <SettingsOutlinedIcon />
        </IconButton>
        <IconButton>
          <MenuOutlinedIcon
            className="person-icon"
            onClick={() => setIsCollapsed((prevState) => !prevState)}
            icon={isCollapsed ? <MenuOutlinedIcon /> : undefined}
          />
        </IconButton>
      </Box>
    </Box>
  );
};

export default Topbar;