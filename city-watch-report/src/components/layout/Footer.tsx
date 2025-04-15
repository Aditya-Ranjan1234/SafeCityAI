
import { Link } from "react-router-dom";
import { AlertTriangle, Facebook, Github, Instagram, Twitter } from "lucide-react";

const Footer = () => {
  return (
    <footer className="border-t bg-background">
      <div className="container py-8 md:py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="md:col-span-1">
            <Link to="/" className="flex items-center gap-2 text-lg font-semibold">
              <AlertTriangle className="h-5 w-5 text-hazard" />
              <span>City Watch Report</span>
            </Link>
            <p className="mt-2 text-sm text-muted-foreground">
              Empowering citizens to report road issues and navigate safely through their city.
            </p>
            <div className="mt-4 flex gap-4">
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Facebook className="h-5 w-5" />
                <span className="sr-only">Facebook</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Twitter className="h-5 w-5" />
                <span className="sr-only">Twitter</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Instagram className="h-5 w-5" />
                <span className="sr-only">Instagram</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Github className="h-5 w-5" />
                <span className="sr-only">GitHub</span>
              </Link>
            </div>
          </div>
          <div>
            <h3 className="text-sm font-medium text-foreground">Features</h3>
            <nav className="mt-4 flex flex-col gap-2 text-sm">
              <Link to="/map" className="text-muted-foreground hover:text-foreground">City Map</Link>
              <Link to="/report" className="text-muted-foreground hover:text-foreground">Report Issues</Link>
              <Link to="/weather" className="text-muted-foreground hover:text-foreground">Weather & Traffic</Link>
              <Link to="/analytics" className="text-muted-foreground hover:text-foreground">City Analytics</Link>
            </nav>
          </div>
          <div>
            <h3 className="text-sm font-medium text-foreground">Resources</h3>
            <nav className="mt-4 flex flex-col gap-2 text-sm">
              <Link to="/faq" className="text-muted-foreground hover:text-foreground">FAQ</Link>
              <Link to="/guidelines" className="text-muted-foreground hover:text-foreground">Reporting Guidelines</Link>
              <Link to="/contact" className="text-muted-foreground hover:text-foreground">Contact Officials</Link>
              <Link to="/statistics" className="text-muted-foreground hover:text-foreground">City Statistics</Link>
            </nav>
          </div>
          <div>
            <h3 className="text-sm font-medium text-foreground">Legal</h3>
            <nav className="mt-4 flex flex-col gap-2 text-sm">
              <Link to="/privacy" className="text-muted-foreground hover:text-foreground">Privacy Policy</Link>
              <Link to="/terms" className="text-muted-foreground hover:text-foreground">Terms of Service</Link>
              <Link to="/cookies" className="text-muted-foreground hover:text-foreground">Cookie Policy</Link>
            </nav>
          </div>
        </div>
        <div className="mt-8 border-t pt-8 text-center text-sm text-muted-foreground">
          <p>&copy; {new Date().getFullYear()} City Watch Report. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
