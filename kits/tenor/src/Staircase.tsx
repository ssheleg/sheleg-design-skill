export interface StaircaseStep {
  /** The two-digit ordinal in the left column. */
  index: string;
  /** One sentence. The measure is 24ch; a second sentence belongs elsewhere. */
  text: string;
}

export interface StaircaseProps {
  /** Exactly four steps. The value ramp has four rungs and no more. */
  steps: [StaircaseStep, StaircaseStep, StaircaseStep, StaircaseStep];
  className?: string;
}

/**
 * The pack's signature element. Four rows, each 3% narrower than the one above
 * and offset 3% further right, each a step darker: --bg, then two neutrals, then
 * --ink with paper text. Rows overlap by -1px so their hairlines share an edge.
 *
 * The type is fixed at four because the ramp is: this is the one place in the
 * pack where the value hierarchy is spent, and a fifth rung would flatten it.
 */
export function Staircase({ steps, className }: StaircaseProps) {
  return (
    <ol className={['tn-stair', className].filter(Boolean).join(' ')}>
      {steps.map((step, i) => (
        <li key={step.index} className={`tn-stair__step tn-stair__step--${i + 1}`}>
          <span className="tn-stair__index">{step.index}</span>
          <p className="tn-stair__text">{step.text}</p>
        </li>
      ))}
    </ol>
  );
}
