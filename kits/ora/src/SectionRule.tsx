export interface SectionRuleProps {
  /** The two-digit ordinal on the chip: 01, 02, 03. */
  index: string;
  /** The section's name. Rendered uppercase and tracked. */
  label: string;
  className?: string;
}

/**
 * The band between two sections: a strip bordered top and bottom, a hand-drawn
 * squiggle through its centre, and a numbered label knocked out over the line.
 * The pack's only ornament, and the reason a long page does not read as a stack
 * of cards.
 */
export function SectionRule({ index, label, className }: SectionRuleProps) {
  return (
    <div className={['ora-sectionrule', className].filter(Boolean).join(' ')} role="separator">
      <svg
        className="ora-sectionrule__wave"
        viewBox="0 0 240 8"
        preserveAspectRatio="none"
        aria-hidden="true"
      >
        <path
          d="M0 4 Q 15 0 30 4 T 60 4 T 90 4 T 120 4 T 150 4 T 180 4 T 210 4 T 240 4"
          fill="none"
          stroke="currentColor"
          strokeWidth="1"
        />
      </svg>
      <span className="ora-sectionrule__chip">
        <span className="ora-sectionrule__index">{index}</span>
        <span className="ora-sectionrule__label">{label}</span>
      </span>
    </div>
  );
}
