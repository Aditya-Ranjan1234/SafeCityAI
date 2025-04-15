
import { useState } from "react";
import { Link } from "react-router-dom";
import { 
  Bell, 
  Menu, 
  Map,
  AlertTriangle, 
  Cloud,
  Search,
  UserCircle
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <header className="sticky top-0 z-40 border-b bg-background/95 backdrop-blur">
      <div className="container flex h-16 items-center justify-between py-4">
        <div className="flex items-center gap-2 md:gap-4">
          <Sheet>
            <SheetTrigger asChild>
              <Button variant="ghost" size="icon" className="md:hidden">
                <Menu className="h-5 w-5" />
                <span className="sr-only">Toggle menu</span>
              </Button>
            </SheetTrigger>
            <SheetContent side="left" className="w-72">
              <nav className="flex flex-col gap-4 pt-4">
                <Link to="/" className="flex items-center gap-2 text-lg font-semibold">
                  <AlertTriangle className="h-5 w-5 text-hazard" />
                  City Watch
                </Link>
                <Link to="/map" className="flex items-center gap-2 px-2 py-1 hover:bg-accent rounded-md">
                  <Map className="h-5 w-5" />
                  <span>City Map</span>
                </Link>
                <Link to="/report" className="flex items-center gap-2 px-2 py-1 hover:bg-accent rounded-md">
                  <AlertTriangle className="h-5 w-5" />
                  <span>Report Issue</span>
                </Link>
                <Link to="/weather" className="flex items-center gap-2 px-2 py-1 hover:bg-accent rounded-md">
                  <Cloud className="h-5 w-5" />
                  <span>Weather & Traffic</span>
                </Link>
                {!isLoggedIn && (
                  <div className="flex gap-2 mt-4">
                    <Button variant="outline" className="w-full" onClick={() => setIsLoggedIn(true)}>
                      Login
                    </Button>
                    <Button className="w-full">Sign up</Button>
                  </div>
                )}
              </nav>
            </SheetContent>
          </Sheet>
          
          <Link to="/" className="flex items-center gap-2 text-lg font-semibold">
            <AlertTriangle className="h-5 w-5 text-hazard" />
            <span className="hidden sm:inline-block">City Watch Report</span>
            <span className="sm:hidden">CityWatch</span>
          </Link>
          
          <nav className="hidden md:flex items-center gap-6 text-sm">
            <Link to="/map" className="transition-colors hover:text-foreground/80 text-foreground/60">City Map</Link>
            <Link to="/report" className="transition-colors hover:text-foreground/80 text-foreground/60">Report Issue</Link>
            <Link to="/weather" className="transition-colors hover:text-foreground/80 text-foreground/60">Weather & Traffic</Link>
          </nav>
        </div>

        <div className="flex items-center gap-2">
          <div className="hidden md:flex relative w-64">
            <Search className="absolute left-2 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input placeholder="Search issues..." className="pl-8" />
          </div>
          
          {isLoggedIn ? (
            <div className="flex items-center gap-4">
              <Button variant="ghost" size="icon">
                <Bell className="h-5 w-5" />
                <span className="sr-only">Notifications</span>
              </Button>
              
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" size="icon" className="rounded-full">
                    <UserCircle className="h-6 w-6" />
                    <span className="sr-only">User menu</span>
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuLabel>My Account</DropdownMenuLabel>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem>Profile</DropdownMenuItem>
                  <DropdownMenuItem>My Reports</DropdownMenuItem>
                  <DropdownMenuItem>Settings</DropdownMenuItem>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem onClick={() => setIsLoggedIn(false)}>Logout</DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          ) : (
            <div className="hidden md:flex gap-2">
              <Button variant="outline" onClick={() => setIsLoggedIn(true)}>Login</Button>
              <Button>Sign up</Button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Navbar;
