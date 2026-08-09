import type { ReactNode } from 'react';

export interface SpecimenProps {
  /** The window title shown beside the three dots. */
  title?: string;
  /** Crop the frame to this height and let the viewport cut the rest. */
  height?: number | string;
  children: ReactNode;
  className?: string;
}

/**
 * The pack's signature: one real product surface, framed, under the
 * seven-layer shadow.
 *
 * Two rules that are easy to break and expensive to break. **One per page** —
 * two exhibits is a catalogue, not a showroom. And **crop, never scale**:
 * shrinking a product surface until it fits makes its chips unreadable and its
 * type stop matching the page around it, at which point it has stopped being
 * evidence and become an illustration of evidence. Pass `height` and let the
 * frame cut off.
 *
 * Inside the frame there are no shadows at all — contents are divided by
 * `--line-weak` hairlines. The stack lifts the frame; hairlines divide what is
 * in it, and they do not swap.
 */
export function Specimen({ title, height, children, className }: SpecimenProps) {
  return (
    <figure
      className={['sw-specimen', className].filter(Boolean).join(' ')}
      style={height !== undefined ? { height } : undefined}
    >
      <div className="sw-specimen__bar">
        <span className="sw-specimen__dots" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
        {title !== undefined && <span className="sw-specimen__title">{title}</span>}
      </div>
      <div className="sw-specimen__body">{children}</div>
    </figure>
  );
}
