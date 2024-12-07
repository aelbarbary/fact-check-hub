export interface Fact {
  id: string;
  statement: string;
  isVerified: boolean;
  verificationStatus: 'pending' | 'verified' | 'false';
  source?: string;
  category: string;
  dateAdded: string;
}