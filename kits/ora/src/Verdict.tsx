import type { ReactNode } from 'react';

export type Grade = 'A+' | 'A' | 'B' | 'C' | 'D' | 'F';

export interface VerdictProps {
  /** The score itself. A string, so a leading zero or an em space survives. */
  score: string;
  /** The denominator, rendered at roughly half the score's size in --muted. */
  outOf?: string;
  grade: Grade;
  /** The word beside the letter. The letter alone is not the message. */
  label: string;
  className?: string;
}

const GRADE_TOKEN: Record<Grade, string> = {
  'A+': 'a-plus',
  A: 'a',
  B: 'b',
  C: 'c',
  D: 'd',
  F: 'f',
};

/**
 * The pack's signature element: one number in the display serif, in its grade
 * colour, with the letter and the word underneath. The letter and the word are
 * required — this is the only place a status colour reaches display size, and it
 * never carries the meaning alone.
 */
export function Verdict({ score, outOf = '100', grade, label, className }: VerdictProps) {
  const tone = `ora-verdict--${GRADE_TOKEN[grade]}`;
  return (
    <div className={['ora-verdict', tone, className].filter(Boolean).join(' ')}>
      <p className="ora-verdict__figure">
        <span className="ora-verdict__score">{score}</span>
        <span className="ora-verdict__out">/ {outOf}</span>
      </p>
      <p className="ora-verdict__grade">
        <span className="ora-verdict__letter">{grade}</span>
        <span className="ora-verdict__label">{label}</span>
      </p>
    </div>
  );
}

export type VerdictChildren = ReactNode;
