import type { ReactNode } from 'react';

export interface ClaimEvidenceProps {
  /** The assertion, in the display face. */
  claim: ReactNode;
  /**
   * The study, trial or register it rests on. Required on purpose: a claim
   * without its citation line is the one thing this pack bans outright.
   */
  source: string;
  className?: string;
}

export function ClaimEvidence({ claim, source, className }: ClaimEvidenceProps) {
  return (
    <div className={['orch-claim', className].filter(Boolean).join(' ')}>
      <p className="orch-claim__claim">{claim}</p>
      <p className="orch-claim__source">
        <cite className="orch-claim__cite">{source}</cite>
      </p>
    </div>
  );
}
