
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import WeatherTraffic from "@/components/weather/WeatherTraffic";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { AlertCircle, AlertTriangle, Calendar, Clock, CloudRain, InfoIcon } from "lucide-react";

const WeatherPage = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <main className="flex-grow py-8">
        <div className="container">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold tracking-tighter">Weather & Traffic</h1>
            <p className="text-muted-foreground mt-2 max-w-2xl mx-auto">
              Get real-time updates on weather conditions and traffic status to plan your journey safely.
            </p>
          </div>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle>Current Conditions</CardTitle>
                  <CardDescription>Updated weather and traffic information</CardDescription>
                </CardHeader>
                <CardContent>
                  <WeatherTraffic />
                </CardContent>
              </Card>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
                <Card>
                  <CardHeader className="pb-2">
                    <div className="flex items-center gap-2">
                      <AlertTriangle className="h-5 w-5 text-hazard" />
                      <CardTitle>Weather Alerts</CardTitle>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div className="p-3 bg-hazard-yellow/10 border border-hazard-yellow/20 rounded-md">
                        <div className="flex items-start gap-2">
                          <AlertCircle className="h-5 w-5 text-hazard-amber mt-0.5" />
                          <div>
                            <h4 className="font-medium text-sm">Heavy Rain Advisory</h4>
                            <p className="text-xs text-muted-foreground mt-1">Potential for street flooding in low-lying areas. Drive with caution.</p>
                            <div className="flex items-center gap-4 mt-2 text-xs text-muted-foreground">
                              <div className="flex items-center gap-1">
                                <Calendar className="h-3 w-3" />
                                <span>Apr 15</span>
                              </div>
                              <div className="flex items-center gap-1">
                                <Clock className="h-3 w-3" />
                                <span>6:00 PM - 11:00 PM</span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      
                      <div className="p-3 border rounded-md">
                        <div className="flex items-start gap-2">
                          <InfoIcon className="h-5 w-5 text-muted-foreground mt-0.5" />
                          <div>
                            <h4 className="font-medium text-sm">High Wind Watch</h4>
                            <p className="text-xs text-muted-foreground mt-1">Winds 25-35 mph with gusts up to 50 mph possible tomorrow.</p>
                            <div className="flex items-center gap-4 mt-2 text-xs text-muted-foreground">
                              <div className="flex items-center gap-1">
                                <Calendar className="h-3 w-3" />
                                <span>Apr 16</span>
                              </div>
                              <div className="flex items-center gap-1">
                                <Clock className="h-3 w-3" />
                                <span>All Day</span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
                
                <Card>
                  <CardHeader className="pb-2">
                    <div className="flex items-center gap-2">
                      <CloudRain className="h-5 w-5 text-civic-blue" />
                      <CardTitle>Rain Impact</CardTitle>
                    </div>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <p className="text-sm text-muted-foreground">
                        Recent rainfall has affected road conditions in several areas of the city.
                        The following locations may experience issues:
                      </p>
                      
                      <ul className="space-y-2 text-sm">
                        <li className="flex items-start gap-2">
                          <AlertCircle className="h-4 w-4 text-hazard-orange mt-0.5" />
                          <span>Downtown underpass - minor flooding reported</span>
                        </li>
                        <li className="flex items-start gap-2">
                          <AlertCircle className="h-4 w-4 text-hazard-orange mt-0.5" />
                          <span>River Road - slippery conditions after rainfall</span>
                        </li>
                        <li className="flex items-start gap-2">
                          <AlertCircle className="h-4 w-4 text-hazard-orange mt-0.5" />
                          <span>Construction site on Oak St - muddy detours</span>
                        </li>
                        <li className="flex items-start gap-2">
                          <AlertCircle className="h-4 w-4 text-hazard-orange mt-0.5" />
                          <span>Highway 101 Exit 24 - standing water in right lane</span>
                        </li>
                      </ul>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
            
            <div className="space-y-6">
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle>Traffic Alerts</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div className="p-3 bg-hazard/10 border border-hazard/20 rounded-md">
                      <div className="flex items-start gap-2">
                        <AlertTriangle className="h-5 w-5 text-hazard mt-0.5" />
                        <div>
                          <h4 className="font-medium text-sm">Major Accident</h4>
                          <p className="text-xs text-muted-foreground mt-1">Highway 101 Northbound at Exit 20. Two lanes blocked. Expect delays of 25+ minutes.</p>
                          <div className="flex items-center gap-4 mt-2 text-xs text-muted-foreground">
                            <div className="flex items-center gap-1">
                              <Clock className="h-3 w-3" />
                              <span>Updated 15 min ago</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <div className="p-3 bg-civic-blue/10 border border-civic-blue/20 rounded-md">
                      <div className="flex items-start gap-2">
                        <InfoIcon className="h-5 w-5 text-civic-blue mt-0.5" />
                        <div>
                          <h4 className="font-medium text-sm">Road Closure</h4>
                          <p className="text-xs text-muted-foreground mt-1">Maple Avenue closed for construction between 5th and 7th Streets until April 20.</p>
                        </div>
                      </div>
                    </div>
                    
                    <div className="p-3 border rounded-md">
                      <div className="flex items-start gap-2">
                        <InfoIcon className="h-5 w-5 text-muted-foreground mt-0.5" />
                        <div>
                          <h4 className="font-medium text-sm">Special Event</h4>
                          <p className="text-xs text-muted-foreground mt-1">City Marathon this weekend. Multiple street closures downtown from 7 AM to 2 PM on Saturday.</p>
                        </div>
                      </div>
                    </div>
                    
                    <div className="p-3 border rounded-md">
                      <div className="flex items-start gap-2">
                        <InfoIcon className="h-5 w-5 text-muted-foreground mt-0.5" />
                        <div>
                          <h4 className="font-medium text-sm">Planned Construction</h4>
                          <p className="text-xs text-muted-foreground mt-1">Bridge maintenance on River Road starts next week. Expect lane restrictions and delays.</p>
                        </div>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
              
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle>Safe Driving Tips</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-3 text-sm">
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Reduce speed during wet or foggy conditions</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Maintain safe following distance (3-second rule)</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Turn on headlights in poor visibility</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Avoid driving through standing water</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Check your route for accidents or closures before leaving</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="font-bold text-civic-blue">•</span>
                      <span>Allow extra time for travel during severe weather</span>
                    </li>
                  </ul>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </main>
      
      <Footer />
    </div>
  );
};

export default WeatherPage;
