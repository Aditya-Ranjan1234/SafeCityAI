
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import ReportIssueForm from "@/components/issues/ReportIssueForm";
import { Card, CardContent } from "@/components/ui/card";
import { AlertTriangle, HelpCircle, Info } from "lucide-react";

const ReportPage = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      
      <main className="flex-grow py-8">
        <div className="container">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold tracking-tighter">Report a Road Issue</h1>
            <p className="text-muted-foreground mt-2 max-w-2xl mx-auto">
              Help improve your city by reporting potholes, construction hazards, 
              and other infrastructure problems for officials to address.
            </p>
          </div>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
              <ReportIssueForm />
            </div>
            
            <div className="space-y-6">
              <Card>
                <CardContent className="p-6">
                  <div className="flex items-start gap-3">
                    <Info className="h-5 w-5 text-primary mt-0.5" />
                    <div>
                      <h3 className="font-semibold mb-2">Reporting Guidelines</h3>
                      <ul className="text-sm text-muted-foreground space-y-2">
                        <li>Be specific about the location and problem</li>
                        <li>Include photos whenever possible</li>
                        <li>Provide measurements if applicable</li>
                        <li>Indicate if the issue is causing immediate danger</li>
                        <li>You can report anonymously or create an account to track updates</li>
                      </ul>
                    </div>
                  </div>
                </CardContent>
              </Card>
              
              <Card>
                <CardContent className="p-6">
                  <div className="flex items-start gap-3">
                    <HelpCircle className="h-5 w-5 text-civic-blue mt-0.5" />
                    <div>
                      <h3 className="font-semibold mb-2">What Happens Next?</h3>
                      <ol className="text-sm text-muted-foreground space-y-2 list-decimal pl-4">
                        <li>Your report is submitted to the appropriate department</li>
                        <li>Officials review and prioritize the issue</li>
                        <li>Work is scheduled based on severity and resources</li>
                        <li>You'll receive updates if you provided contact information</li>
                        <li>Once resolved, the status will be updated on the map</li>
                      </ol>
                    </div>
                  </div>
                </CardContent>
              </Card>
              
              <Card className="bg-hazard/10 border-hazard/20">
                <CardContent className="p-6">
                  <div className="flex items-start gap-3">
                    <AlertTriangle className="h-5 w-5 text-hazard mt-0.5" />
                    <div>
                      <h3 className="font-semibold mb-2">Emergency Situations</h3>
                      <p className="text-sm text-muted-foreground mb-3">
                        This platform is not for reporting emergencies. For situations requiring immediate attention:
                      </p>
                      <ul className="text-sm font-medium space-y-1">
                        <li>Call 911 for accidents or life-threatening situations</li>
                        <li>Contact city services directly at (555) 123-4567 for urgent issues</li>
                      </ul>
                    </div>
                  </div>
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

export default ReportPage;
