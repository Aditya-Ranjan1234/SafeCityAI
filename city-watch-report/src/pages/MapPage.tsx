
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import CityMap from "@/components/map/CityMap";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { AlertTriangle, ArrowRight, Filter, Map, MapPin } from "lucide-react";
import { Link } from "react-router-dom";

const MapPage = () => {
  // This would fetch from an API in a real application
  const accidentHotspots = [
    {
      id: "1",
      name: "Junction Road & Main Street",
      incidents: 15,
      severity: "high",
      description: "Poor visibility at night, lack of proper signage",
    },
    {
      id: "2",
      name: "Highway 101 Exit 24",
      incidents: 8,
      severity: "medium",
      description: "Sharp curve with inadequate warning signs",
    },
    {
      id: "3",
      name: "Downtown Bridge Entrance",
      incidents: 12,
      severity: "high",
      description: "Slippery when wet, no guard rails",
    },
    {
      id: "4",
      name: "School Zone on Oak Avenue",
      incidents: 6,
      severity: "medium",
      description: "Speeding vehicles despite school zone warnings",
    },
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <main className="flex-grow">
        <div className="container py-8">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6">
            <div>
              <h1 className="text-3xl font-bold tracking-tighter">City Map</h1>
              <p className="text-muted-foreground mt-2">
                Explore reported issues and accident-prone areas in your city
              </p>
            </div>
            
            <div className="flex gap-2 mt-4 md:mt-0">
              <Button variant="outline" size="sm">
                <Filter className="h-4 w-4 mr-2" />
                Filter
              </Button>
              <Button size="sm" asChild>
                <Link to="/report">
                  <AlertTriangle className="h-4 w-4 mr-2" />
                  Report Issue
                </Link>
              </Button>
            </div>
          </div>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <Card className="overflow-hidden">
                <CardContent className="p-0">
                  <CityMap centerLat={40.7128} centerLng={-74.006} zoom={13} />
                </CardContent>
              </Card>
            </div>
            
            <div>
              <Tabs defaultValue="hotspots">
                <TabsList className="grid w-full grid-cols-2">
                  <TabsTrigger value="hotspots">Accident Hotspots</TabsTrigger>
                  <TabsTrigger value="issues">Reported Issues</TabsTrigger>
                </TabsList>
                
                <TabsContent value="hotspots" className="mt-4">
                  <Card>
                    <CardContent className="p-4">
                      <div className="space-y-4">
                        <div className="flex items-center justify-between">
                          <h3 className="font-medium">Accident-Prone Areas</h3>
                          <Badge variant="outline" className="text-xs">
                            {accidentHotspots.length} Areas
                          </Badge>
                        </div>
                        
                        <div className="space-y-3 max-h-[400px] overflow-y-auto pr-2">
                          {accidentHotspots.map((hotspot) => (
                            <div key={hotspot.id} className="border rounded-lg p-3 hover:bg-accent/50 transition-colors">
                              <div className="flex items-start justify-between">
                                <div className="flex items-start gap-2">
                                  <div className="mt-0.5">
                                    <Map className="h-4 w-4 text-muted-foreground" />
                                  </div>
                                  <div>
                                    <h4 className="font-medium text-sm">{hotspot.name}</h4>
                                    <p className="text-xs text-muted-foreground mt-1">{hotspot.description}</p>
                                  </div>
                                </div>
                                <Badge 
                                  className={
                                    hotspot.severity === "high" 
                                      ? "bg-hazard text-white"
                                      : hotspot.severity === "medium"
                                      ? "bg-hazard-orange text-white"
                                      : "bg-hazard-yellow text-black"
                                  }
                                >
                                  {hotspot.incidents} incidents
                                </Badge>
                              </div>
                              <Button variant="ghost" size="sm" className="w-full mt-2 h-8 text-xs">
                                View Details
                                <ArrowRight className="h-3 w-3 ml-1" />
                              </Button>
                            </div>
                          ))}
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </TabsContent>
                
                <TabsContent value="issues" className="mt-4">
                  <Card>
                    <CardContent className="p-4">
                      <div className="space-y-4">
                        <div className="flex items-center justify-between">
                          <h3 className="font-medium">Recent Issues</h3>
                          <Link to="/issues" className="text-xs text-primary hover:underline">
                            View All
                          </Link>
                        </div>
                        
                        <div className="space-y-3 max-h-[400px] overflow-y-auto pr-2">
                          {/* This would come from your API in a real app */}
                          {[1, 2, 3, 4, 5].map((i) => (
                            <div key={i} className="border rounded-lg p-3 hover:bg-accent/50 transition-colors">
                              <div className="flex items-start gap-3">
                                <div className="flex-shrink-0 mt-1">
                                  <AlertTriangle className="h-4 w-4 text-hazard" />
                                </div>
                                <div>
                                  <h4 className="font-medium text-sm">
                                    {i % 2 === 0 ? "Pothole on Cedar Avenue" : "Broken Street Light"}
                                  </h4>
                                  <div className="flex items-center gap-1 mt-1">
                                    <MapPin className="h-3 w-3 text-muted-foreground" />
                                    <span className="text-xs text-muted-foreground">
                                      {i % 2 === 0 ? "Cedar Ave & 10th St" : "Park Boulevard"}
                                    </span>
                                  </div>
                                  <div className="flex items-center gap-2 mt-2">
                                    <Badge variant="outline" className="text-xs">
                                      {i % 3 === 0 ? "Construction" : i % 2 === 0 ? "Pothole" : "Lighting"}
                                    </Badge>
                                    <Badge 
                                      className={`text-xs ${
                                        i % 3 === 0 
                                          ? "bg-hazard text-white" 
                                          : i % 2 === 0 
                                          ? "bg-hazard-orange text-white" 
                                          : "bg-hazard-yellow text-black"
                                      }`}
                                    >
                                      {i % 3 === 0 ? "High" : i % 2 === 0 ? "Medium" : "Low"}
                                    </Badge>
                                  </div>
                                </div>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </TabsContent>
              </Tabs>
            </div>
          </div>
        </div>
      </main>
      
      <Footer />
    </div>
  );
};

export default MapPage;
