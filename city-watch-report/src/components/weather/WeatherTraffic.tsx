
import { Cloud, CloudRain, CloudSnow, CloudSun, Droplets, Sun, SunDim, Wind } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const WeatherTraffic = () => {
  // In a real app, these would come from a weather API
  const weatherData = {
    current: {
      temperature: 72,
      condition: "sunny",
      humidity: 45,
      windSpeed: 8,
      precipitation: 0,
      feelsLike: 75,
    },
    forecast: [
      { day: "Today", high: 74, low: 62, condition: "sunny" },
      { day: "Tomorrow", high: 70, low: 60, condition: "partly-cloudy" },
      { day: "Wednesday", high: 68, low: 58, condition: "rainy" },
      { day: "Thursday", high: 65, low: 55, condition: "cloudy" },
      { day: "Friday", high: 72, low: 60, condition: "sunny" },
    ],
  };

  // These would come from a traffic API
  const trafficData = {
    routes: [
      { 
        name: "Downtown to Uptown", 
        congestion: "moderate", 
        travelTime: "25 min",
        normalTime: "18 min",
        incidents: 1 
      },
      { 
        name: "North to South Highway", 
        congestion: "heavy", 
        travelTime: "45 min",
        normalTime: "22 min",
        incidents: 3 
      },
      { 
        name: "East to West Corridor", 
        congestion: "light", 
        travelTime: "15 min",
        normalTime: "14 min",
        incidents: 0 
      },
      { 
        name: "River Crossing Bridge", 
        congestion: "severe", 
        travelTime: "35 min",
        normalTime: "12 min",
        incidents: 2 
      },
    ],
  };

  const getWeatherIcon = (condition: string) => {
    switch (condition) {
      case "sunny":
        return <Sun className="h-6 w-6 text-amber-500" />;
      case "partly-cloudy":
        return <CloudSun className="h-6 w-6 text-amber-400" />;
      case "cloudy":
        return <Cloud className="h-6 w-6 text-gray-400" />;
      case "rainy":
        return <CloudRain className="h-6 w-6 text-blue-400" />;
      case "snowy":
        return <CloudSnow className="h-6 w-6 text-blue-200" />;
      case "foggy":
        return <SunDim className="h-6 w-6 text-gray-300" />;
      default:
        return <Sun className="h-6 w-6 text-amber-500" />;
    }
  };

  const getCongestionColor = (congestion: string) => {
    switch (congestion) {
      case "light":
        return "text-green-500";
      case "moderate":
        return "text-amber-500";
      case "heavy":
        return "text-orange-500";
      case "severe":
        return "text-red-600";
      default:
        return "text-gray-500";
    }
  };

  const getCongestionProgress = (congestion: string) => {
    switch (congestion) {
      case "light":
        return 25;
      case "moderate":
        return 50;
      case "heavy":
        return 75;
      case "severe":
        return 95;
      default:
        return 0;
    }
  };

  const getProgressColor = (congestion: string) => {
    switch (congestion) {
      case "light":
        return "bg-green-500";
      case "moderate":
        return "bg-amber-500";
      case "heavy":
        return "bg-orange-500";
      case "severe":
        return "bg-red-600";
      default:
        return "bg-gray-500";
    }
  };

  return (
    <Tabs defaultValue="weather" className="w-full">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="weather">Weather</TabsTrigger>
        <TabsTrigger value="traffic">Traffic</TabsTrigger>
      </TabsList>
      
      <TabsContent value="weather" className="mt-4">
        <Card className="border-0 shadow-none">
          <CardHeader className="pb-2">
            <CardTitle>Current Weather</CardTitle>
            <CardDescription>Updated weather conditions for your city</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">
                <div>
                  <p className="text-4xl font-bold">{weatherData.current.temperature}°F</p>
                  <p className="text-muted-foreground capitalize">Feels like {weatherData.current.feelsLike}°F</p>
                </div>
                <div className="text-center">
                  {getWeatherIcon(weatherData.current.condition)}
                  <p className="mt-1 capitalize">{weatherData.current.condition}</p>
                </div>
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <Card className="shadow-sm">
                  <CardContent className="p-4 flex items-center gap-3">
                    <Droplets className="h-5 w-5 text-blue-500" />
                    <div>
                      <p className="text-sm text-muted-foreground">Humidity</p>
                      <p className="font-medium">{weatherData.current.humidity}%</p>
                    </div>
                  </CardContent>
                </Card>
                
                <Card className="shadow-sm">
                  <CardContent className="p-4 flex items-center gap-3">
                    <Wind className="h-5 w-5 text-cyan-500" />
                    <div>
                      <p className="text-sm text-muted-foreground">Wind</p>
                      <p className="font-medium">{weatherData.current.windSpeed} mph</p>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
            
            <div className="mt-8">
              <h3 className="text-lg font-medium mb-4">5-Day Forecast</h3>
              <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
                {weatherData.forecast.map((day) => (
                  <Card key={day.day} className="shadow-sm">
                    <CardContent className="p-4 flex flex-col items-center text-center">
                      <p className="font-medium">{day.day}</p>
                      {getWeatherIcon(day.condition)}
                      <div className="mt-2 flex gap-2 text-sm">
                        <span className="font-medium">{day.high}°</span>
                        <span className="text-muted-foreground">{day.low}°</span>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      </TabsContent>
      
      <TabsContent value="traffic" className="mt-4">
        <Card className="border-0 shadow-none">
          <CardHeader className="pb-2">
            <CardTitle>Live Traffic Conditions</CardTitle>
            <CardDescription>Current traffic status on major routes</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-6">
              {trafficData.routes.map((route) => (
                <div key={route.name} className="border rounded-lg p-4">
                  <div className="flex justify-between items-start mb-3">
                    <div>
                      <h3 className="font-medium">{route.name}</h3>
                      <p className="text-sm text-muted-foreground">
                        Current: <span className="font-medium">{route.travelTime}</span> (normally {route.normalTime})
                      </p>
                    </div>
                    <div className={`text-sm font-semibold uppercase ${getCongestionColor(route.congestion)}`}>
                      {route.congestion}
                    </div>
                  </div>
                  
                  <Progress 
                    value={getCongestionProgress(route.congestion)} 
                    className="h-2 bg-gray-200" 
                    indicatorClassName={getProgressColor(route.congestion)}
                  />
                  
                  {route.incidents > 0 && (
                    <div className="mt-3 flex items-center gap-1 text-sm text-red-600">
                      <AlertCircle className="h-4 w-4" />
                      {route.incidents} {route.incidents === 1 ? 'incident' : 'incidents'} reported
                    </div>
                  )}
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </TabsContent>
    </Tabs>
  );
};

export default WeatherTraffic;
