
import { AlertCircle, ChevronsRight, MapPin, ThumbsUp, MessageSquare } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardFooter, CardHeader } from "@/components/ui/card";
import { cn } from "@/lib/utils";

export interface IssueCardProps {
  id: string;
  title: string;
  description: string;
  location: string;
  type: 'pothole' | 'construction' | 'accident' | 'other';
  severity: 'low' | 'medium' | 'high';
  dateReported: string;
  upvotes: number;
  comments: number;
  imageUrl?: string;
  status: 'open' | 'in-progress' | 'resolved';
}

const IssueCard: React.FC<IssueCardProps> = ({
  id,
  title,
  description,
  location,
  type,
  severity,
  dateReported,
  upvotes,
  comments,
  imageUrl,
  status,
}) => {
  const getTypeLabel = (type: string) => {
    switch (type) {
      case 'pothole':
        return 'Pothole';
      case 'construction':
        return 'Incomplete Construction';
      case 'accident':
        return 'Accident Prone Area';
      default:
        return 'Other Issue';
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'open':
        return 'bg-red-100 text-red-800 border-red-200';
      case 'in-progress':
        return 'bg-blue-100 text-blue-800 border-blue-200';
      case 'resolved':
        return 'bg-green-100 text-green-800 border-green-200';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200';
    }
  };
  
  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'high':
        return 'bg-hazard text-white';
      case 'medium':
        return 'bg-hazard-orange text-white';
      case 'low':
        return 'bg-hazard-yellow text-black';
      default:
        return 'bg-muted text-muted-foreground';
    }
  };

  return (
    <Card className="h-full flex flex-col hover:shadow-md transition-all duration-200 overflow-hidden">
      {imageUrl && (
        <div className="relative h-48 w-full">
          <img 
            src={imageUrl} 
            alt={title} 
            className="w-full h-full object-cover"
          />
          <div className="absolute top-2 right-2">
            <Badge variant="secondary" className={cn("text-xs capitalize", getStatusColor(status))}>
              {status.replace('-', ' ')}
            </Badge>
          </div>
        </div>
      )}
      
      <CardHeader className={!imageUrl ? "relative pb-0" : "pb-0"}>
        {!imageUrl && (
          <div className="absolute top-4 right-4">
            <Badge variant="secondary" className={cn("text-xs capitalize", getStatusColor(status))}>
              {status.replace('-', ' ')}
            </Badge>
          </div>
        )}
        
        <div className="flex items-center gap-2 mb-2">
          <Badge className={cn("text-xs", getSeverityColor(severity))}>
            {severity.charAt(0).toUpperCase() + severity.slice(1)} Severity
          </Badge>
          <Badge variant="outline" className="text-xs">
            {getTypeLabel(type)}
          </Badge>
        </div>
        
        <h3 className="text-lg font-semibold line-clamp-1">{title}</h3>
        
        <div className="flex items-center text-xs text-muted-foreground gap-1 mt-1">
          <MapPin className="h-3 w-3" />
          <span className="truncate">{location}</span>
        </div>
      </CardHeader>
      
      <CardContent className="py-4 flex-grow">
        <p className="text-sm text-muted-foreground line-clamp-3">{description}</p>
      </CardContent>
      
      <CardFooter className="pt-0 flex items-center justify-between">
        <div className="flex items-center gap-4 text-sm text-muted-foreground">
          <div className="flex items-center gap-1">
            <ThumbsUp className="h-4 w-4" />
            <span>{upvotes}</span>
          </div>
          <div className="flex items-center gap-1">
            <MessageSquare className="h-4 w-4" />
            <span>{comments}</span>
          </div>
        </div>
        
        <Button variant="ghost" size="sm" className="p-0 h-auto">
          <span className="text-sm">Details</span>
          <ChevronsRight className="h-4 w-4 ml-1" />
        </Button>
      </CardFooter>
    </Card>
  );
};

export default IssueCard;
