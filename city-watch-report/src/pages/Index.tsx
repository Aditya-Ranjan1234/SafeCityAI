
import { Link } from "react-router-dom";
import { ArrowRight, AlertTriangle, MapPin, Upload, CloudRain, Shield } from "lucide-react";
import { Button } from "@/components/ui/button";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import CityMap from "@/components/map/CityMap";
import IssueCard from "@/components/issues/IssueCard";

// Sample issue data for the homepage
const SAMPLE_ISSUES = [
  {
    id: "1",
    title: "Deep pothole causing vehicle damage",
    description: "A large pothole near the intersection has damaged multiple vehicles. It's approximately 2 feet wide and 8 inches deep.",
    location: "Main St & 5th Ave intersection",
    type: "pothole" as const,
    severity: "high" as const,
    dateReported: "2023-04-10",
    upvotes: 24,
    comments: 7,
    imageUrl: "https://images.unsplash.com/photo-1596726047970-af3fe860dae2?q=80&w=500&auto=format&fit=crop",
    status: "open" as const,
  },
  {
    id: "2",
    title: "Abandoned construction site",
    description: "This sidewalk construction has been abandoned for weeks. The site is dangerous for pedestrians and causing accessibility issues.",
    location: "Highland Park, near Community Center",
    type: "construction" as const,
    severity: "medium" as const,
    dateReported: "2023-04-05",
    upvotes: 18,
    comments: 5,
    imageUrl: "https://images.unsplash.com/photo-1503669678209-c68d00b3765d?q=80&w=500&auto=format&fit=crop",
    status: "in-progress" as const,
  },
  {
    id: "3",
    title: "Dangerous intersection",
    description: "This intersection has had 5 accidents in the past month. Visibility is poor and there are no proper traffic signs.",
    location: "Oak Street & River Road",
    type: "accident" as const,
    severity: "high" as const,
    dateReported: "2023-04-12",
    upvotes: 42,
    comments: 12,
    imageUrl: "https://images.unsplash.com/photo-1465447142348-e9952c393450?q=80&w=500&auto=format&fit=crop",
    status: "open" as const,
  },
];

const Index = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="relative py-20 bg-gradient-to-b from-civic-blue/20 to-background">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
              <div className="space-y-4">
                <div className="inline-block rounded-lg bg-civic-blue/10 px-3 py-1 text-sm text-civic-blue">
                  Community-driven road safety
                </div>
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
                  Report City Issues, Navigate Safely
                </h1>
                <p className="text-muted-foreground md:text-xl">
                  Help improve your city by reporting road issues like potholes and broken infrastructure.
                  Get real-time updates on traffic, weather, and accident-prone areas.
                </p>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button size="lg" asChild>
                    <Link to="/report">
                      Report an Issue
                      <ArrowRight className="ml-2 h-4 w-4" />
                    </Link>
                  </Button>
                  <Button size="lg" variant="outline" asChild>
                    <Link to="/map">Explore City Map</Link>
                  </Button>
                </div>
              </div>
              <div className="mx-auto w-full max-w-[500px] lg:max-w-none rounded-lg overflow-hidden shadow-xl">
                <CityMap centerLat={40.7128} centerLng={-74.006} zoom={12} />
              </div>
            </div>
          </div>
        </section>
        
        {/* Features Section */}
        <section className="py-16 bg-background" id="features">
          <div className="container px-4 md:px-6">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold tracking-tighter">Key Features</h2>
              <p className="text-muted-foreground mt-4 mx-auto max-w-[700px]">
                Our platform provides essential tools for citizens and officials to improve road safety and infrastructure.
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-hazard/10 text-hazard mb-4">
                  <AlertTriangle className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Report Road Issues</h3>
                <p className="text-muted-foreground">
                  Easily report potholes, construction hazards, and other infrastructure problems.
                </p>
              </div>
              
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-civic-blue/10 text-civic-blue mb-4">
                  <MapPin className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Interactive Map</h3>
                <p className="text-muted-foreground">
                  View accident-prone areas, reported issues, and navigate safely through your city.
                </p>
              </div>
              
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-civic-teal/10 text-civic-teal mb-4">
                  <Upload className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Upload Evidence</h3>
                <p className="text-muted-foreground">
                  Add photos to your reports to provide clear evidence of issues for faster resolution.
                </p>
              </div>
              
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-hazard-amber/10 text-hazard-amber mb-4">
                  <CloudRain className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Weather Updates</h3>
                <p className="text-muted-foreground">
                  Stay informed about current weather conditions that might affect your commute.
                </p>
              </div>
              
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-hazard-orange/10 text-hazard-orange mb-4">
                  <Shield className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Traffic Monitoring</h3>
                <p className="text-muted-foreground">
                  Real-time traffic updates to help you avoid congestion and plan your route.
                </p>
              </div>
              
              <div className="flex flex-col items-center text-center p-6 bg-card rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-civic-deepBlue/10 text-civic-deepBlue mb-4">
                  <Shield className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Official Response</h3>
                <p className="text-muted-foreground">
                  Government officials can respond to and update the status of reported issues.
                </p>
              </div>
            </div>
          </div>
        </section>
        
        {/* Recent Issues Section */}
        <section className="py-16 bg-muted/30">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8">
              <div>
                <h2 className="text-3xl font-bold tracking-tighter">Recent Reports</h2>
                <p className="text-muted-foreground mt-2">
                  Latest issues reported in your community
                </p>
              </div>
              <Button className="mt-4 md:mt-0" variant="outline" asChild>
                <Link to="/issues">
                  View All Reports
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
              </Button>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {SAMPLE_ISSUES.map((issue) => (
                <IssueCard key={issue.id} {...issue} />
              ))}
            </div>
          </div>
        </section>
        
        {/* CTA Section */}
        <section className="py-20 bg-civic-blue text-white">
          <div className="container px-4 md:px-6 text-center">
            <h2 className="text-3xl font-bold tracking-tighter mb-4">Join the Community</h2>
            <p className="text-lg text-white/80 mb-6 max-w-[600px] mx-auto">
              Help make your city safer by reporting issues and staying informed about road conditions.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" variant="secondary" asChild>
                <Link to="/register">Create an Account</Link>
              </Button>
              <Button size="lg" variant="outline" className="text-white border-white hover:bg-white/20" asChild>
                <Link to="/about">Learn More</Link>
              </Button>
            </div>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default Index;
